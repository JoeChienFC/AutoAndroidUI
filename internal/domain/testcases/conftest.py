import base64
import datetime
import os
import subprocess
import shutil
import time

import pytest_html
import requests
import json
from PIL import Image
import pytest
import uiautomator2 as u2
from internal.infra.adb.adb_function import ADBClient
from pytest_metadata.plugin import metadata_key

LARK_WEBHOOK_URL = "https://open.larksuite.com/open-apis/bot/v2/hook/5d17525b-a9c3-4f65-ab66-5233cda0ae00"
REPORT_UPLOAD_PATH = r"C:\Users\fanchiao.chien\PycharmProjects\UIAutomation4Android\internal\domain\reports\gallery_all_report.html"
RESIZE_FACTOR = 0.25


class LarkReporter:
    def __init__(self):
        self.webhook_url = LARK_WEBHOOK_URL
        self.test_results = {
            'passed': 0,
            'failed': 0,
            'skipped': 0,
            'total': 0,
            'failed_cases': []
        }

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
        print(f"Preparing to send report to Lark...")

        report_title = self._get_report_title()

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
                            "content": self._generate_report_summary()
                        }
                    }
                ]
            }
        }

        print(f"Test results: {self.test_results}")
        self._send_lark_message(message)

    def _get_report_title(self):
        import sys
        if "-m" in sys.argv and "P0" in sys.argv:
            return "NTGallery P0 自动化测试报告"
        elif "S" in sys.argv:
            return "NTGallery UI Layout 自动化测试报告"
        else:
            return "NTGallery All 自動化測試報告"

    def _generate_report_summary(self):
        if self.test_results['failed'] > 0:
            return f"""
**測試執行時間：** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**測試結果摘要：**
- 總測試數：{self.test_results['total']}
- 通過：{self.test_results['passed']}
- 失敗：{self.test_results['failed']}
- 跳過：{self.test_results['skipped']}

**報告路徑：**
📂 [{REPORT_UPLOAD_PATH}]({REPORT_UPLOAD_PATH})

😱😱  **請注意：**  😱😱
有測試用例未通過，請查閱報告以了解詳細信息😵‍💫😵‍💫😵‍💫
"""
        else:
            return f"""
**測試執行時間：** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**測試結果摘要：**
- 總測試數：{self.test_results['total']}
- 通過：{self.test_results['passed']}
- 失敗：{self.test_results['failed']}
- 跳過：{self.test_results['skipped']}

**恭喜！所有測試通過！**
🎉 **優秀表現！** 🎉
所有測試用例都成功執行，系統運行穩定。感謝您的辛勤工作與努力！繼續保持這樣的表現，我們將邁向更加完美的成果！👏👏

"""

    def _send_lark_message(self, message):
        try:
            print(f"Sending request to Lark...")
            response = requests.post(
                self.webhook_url,
                headers={'Content-Type': 'application/json'},
                data=json.dumps(message),
                timeout=10  # Set timeout to 10 seconds
            )
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.text}")
            if response.status_code == 200:
                print("Successfully sent report to Lark")
            else:
                print(f"Failed to send report to Lark. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending report to Lark: {str(e)}")


# Initialize the global LarkReporter instance
lark_reporter = LarkReporter()


def pytest_html_report_title(report):
    report.title = lark_reporter._get_report_title()


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

    # Update Lark report stats
    lark_reporter.update_stats(report)

    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            capture_screenshot(report, extra)

        report.extra = extra


def capture_screenshot(report, extra):
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
            new_size = (int(img.width * RESIZE_FACTOR), int(img.height * RESIZE_FACTOR))
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
    # original_report_file = "../reports/gallery_all_report.html"

    try:
        # rename_report_file(original_report_file)
        print("Sending report to Lark...")
        lark_reporter.send_report()
        print("Report sent.")
    except Exception as e:
        print(f"Failed to process and upload report: {e}")
