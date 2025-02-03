import base64
import datetime
import os
import subprocess
import time
from PIL import Image
import pytest
import uiautomator2 as u2
from internal.infra.adb.adb_function import ADBClient
import pytest_html
from pytest_metadata.plugin import metadata_key
import shutil
import requests
import json

LARK_WEBHOOK_URL = "https://open.larksuite.com/open-apis/bot/v2/hook/5d17525b-a9c3-4f65-ab66-5233cda0ae00"


class LarkReporter:
    def __init__(self):
        # 直接使用確認過的 URL，而不是從環境變量獲取
        self.webhook_url = LARK_WEBHOOK_URL
        self.test_results = {
            'passed': 0,
            'failed': 0,
            'skipped': 0,
            'total': 0,
            'failed_cases': []
        }
        # 定義報告上傳路徑
        self.report_upload_path = r"\\172.30.1.98\public01\Quality Management\Test Engineering\OS测试资源\Nothing_Gallery\auto_test_report"

    def update_stats(self, report):
        if report.when == "call":
            self.test_results['total'] += 1
            if report.passed:
                self.test_results['passed'] += 1
            elif report.failed:
                self.test_results['failed'] += 1
                self.test_results['failed_cases'].append({
                    'name': report.nodeid,
                    'error': str(getattr(report, 'longrepr', ''))
                })
            elif report.skipped:
                self.test_results['skipped'] += 1

    def send_report(self):
        # 移除不正確的條件檢查
        print(f"Preparing to send report to Lark...")  # 添加除錯信息

        # 取得測試報告標題
        import sys
        if "-m" in sys.argv and "P0" in sys.argv:
            report_title = "NTGallery P0 自动化测试报告"
        elif "S" in sys.argv:
            report_title = "NTGallery UI Layout 自动化测试报告"
        else:
            report_title = "NTGallery All 自動化測試報告"

        message = {
            "msg_type": "interactive",
            "card": {
                "config": {
                    "wide_screen_mode": True
                },
                "header": {
                    "title": {
                        "tag": "plain_text",
                        "content": f"🤖 {report_title}"
                    },
                    "template": "blue" if self.test_results['failed'] == 0 else "red"
                },
                "elements": [
                    {
                        "tag": "div",
                        "text": {
                            "tag": "lark_md",
                            "content": f"""
**測試執行時間：** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**測試結果摘要：**
- 總測試數：{self.test_results['total']}
- 通過：{self.test_results['passed']}
- 失敗：{self.test_results['failed']}
- 跳過：{self.test_results['skipped']}

**報告路徑：**
📂 [{self.report_upload_path}]({self.report_upload_path})
"""
                        }
                    }
                ]
            }
        }

        # 添加除錯信息
        print(f"Test results: {self.test_results}")

        try:
            print(f"Sending request to Lark...")
            response = requests.post(
                self.webhook_url,
                headers={'Content-Type': 'application/json'},
                data=json.dumps(message),
                timeout=10  # 設置超時時間為 10 秒
            )
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.text}")
            if response.status_code == 200:
                print("Successfully sent report to Lark")
            else:
                print(f"Failed to send report to Lark. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending report to Lark: {str(e)}")


# 初始化全局的 LarkReporter 實例
lark_reporter = LarkReporter()


def pytest_html_report_title(report):
    import sys
    if "-m" in sys.argv and "P0" in sys.argv:
        report.title = "NGallery P0 自动化测试报告"
    elif "S" in sys.argv:
        report.title = "NGallery UI Layout 自动化测试报告"
    else:
        report.title = "NGallery All 自動化測試報告"


def pytest_itemcollected(item):
    test_name = item.name
    item._nodeid = test_name


def pytest_configure(config):
    config.stash[metadata_key]["開始時間"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@pytest.fixture(autouse=True)
def restore_environment():
    ADBClient.stop_gallery_app()
    ADBClient.clear_gallery_cache()
    time.sleep(2)
    d = u2.connect()
    d.set_fastinput_ime(True)

    yield

    ADBClient.stop_gallery_app()
    ADBClient.delete_albums_camera_data()
    ADBClient.refresh_gallery_camera()
    ADBClient.refresh_gallery_albums()
    time.sleep(1)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    resize_factor = 0.25

    # 更新 Lark 報告統計
    lark_reporter.update_stats(report)

    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_png_name = f"screenshot_{timestamp}.png"
            screenshot_jpg_name = f"screenshot_{timestamp}.jpg"
            local_png_path = os.path.join(os.getcwd(), screenshot_png_name)
            local_jpg_path = os.path.join(os.getcwd(), screenshot_jpg_name)
            try:
                subprocess.run(["adb", "shell", "screencap", "-p", f"/sdcard/{screenshot_png_name}"])
                subprocess.run(["adb", "pull", f"/sdcard/{screenshot_png_name}", local_png_path], check=True)
                subprocess.run(["adb", "shell", "rm", f"/sdcard/{screenshot_png_name}"])
                ADBClient.refresh_gallery_albums()

                with Image.open(local_png_path) as img:
                    new_size = (int(img.width * resize_factor), int(img.height * resize_factor))
                    img = img.resize(new_size, Image.LANCZOS)
                    rgb_im = img.convert('RGB')
                    rgb_im.save(local_jpg_path, "JPEG")

                with open(local_jpg_path, "rb") as image_file:
                    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
                img_html = f"""
                    <div style="float: right; margin-left: 20px;">
                        <a> 
                            <img src="data:image/jpeg;base64,{image_base64}" style="max-width:300px; max-height:300px;" />
                        </a>
                    </div>
                """
                extra.append(pytest_html.extras.html(img_html))

                os.remove(local_png_path)
                os.remove(local_jpg_path)
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")

        report.extra = extra


def rename_report_file(file_path):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    base, ext = os.path.splitext(file_path)
    new_file_path = f"{base}_{timestamp}{ext}"
    os.rename(file_path, new_file_path)
    return new_file_path


def upload_file_to_network(file_path, network_path):
    shutil.copy(file_path, network_path)


def pytest_html_results_summary(prefix, summary, postfix):
    print("HTML report generation completed. Proceeding with file operations...")
    original_report_file = "../reports/gallery_all_report.html"
    network_path = r"\\172.30.1.98\public01\Quality Management\Test Engineering\OS测试资源\Nothing_Gallery\auto_test_report"

    try:
        new_report_file = rename_report_file(original_report_file)
        upload_file_to_network(new_report_file, network_path)
        print(f"Report has been renamed and uploaded to network path: {network_path}")
    except Exception as e:
        print(f"Failed to process and upload report: {e}")



def pytest_sessionfinish(session, exitstatus):
    print("Waiting for report generation to complete...")
    time.sleep(10)  # 等待 10 秒以確保報告完成

    print("Sending report to Lark...")
    lark_reporter.send_report()
    print("Report sent.")
    # 原始報告檔案處理
    original_report_file = "../reports/gallery_all_report.html"
    network_path = r"\\172.30.1.98\public01\Quality Management\Test Engineering\OS测试资源\Nothing_Gallery\auto_test_report"

    try:
        new_report_file = rename_report_file(original_report_file)
        upload_file_to_network(new_report_file, network_path)
        print(f"Report has been renamed and uploaded to network path: {network_path}\n")
    except Exception as e:
        print(f"Failed to process and upload report: {e}\n")
