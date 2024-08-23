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


def pytest_html_report_title(report):
    import sys
    if "-m" in sys.argv and "P0" in sys.argv:
        report.title = "NGallery P0 自动化测试报告"
    else:
        report.title = "NGallery All 自動化測試報告"


def pytest_configure(config):

    config.stash[metadata_key]["開始時間"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@pytest.fixture(autouse=True)
def restore_environment():
    ADBClient.stop_gallery_app()
    ADBClient.clear_gallery_cache()
    time.sleep(2)
    d = u2.connect()
    d.set_fastinput_ime(True)
    # 測試前執行

    yield
    ADBClient.stop_gallery_app()
    # ADBClient.delete_albums_camera_data()
    time.sleep(1)
    # 測試後執行


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    resize_factor = 0.25

    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 如果测试失败，执行 adb 命令截取屏幕
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_png_name = f"screenshot_{timestamp}.png"
            screenshot_jpg_name = f"screenshot_{timestamp}.jpg"
            local_png_path = os.path.join(os.getcwd(), screenshot_png_name)
            local_jpg_path = os.path.join(os.getcwd(), screenshot_jpg_name)
            try:
                # pytest.set_trace()
                # 使用 adb 截取屏幕并将其保存到本地文件
                subprocess.run(["adb", "shell", "screencap", "-p", f"/sdcard/{screenshot_png_name}"])
                print(f"Local screenshot path: {local_png_path}")
                subprocess.run(["adb", "pull", f"/sdcard/{screenshot_png_name}", local_png_path], check=True)
                print(f"Screenshot pulled to: {local_png_path}")

                subprocess.run(["adb", "shell", "rm", f"/sdcard/{screenshot_png_name}"])
                print(f"Delete fail screenshot: {screenshot_png_name}")

                with Image.open(local_png_path) as img:
                    new_size = (int(img.width * resize_factor), int(img.height * resize_factor))
                    img = img.resize(new_size, Image.LANCZOS)
                    rgb_im = img.convert('RGB')
                    rgb_im.save(local_jpg_path, "JPEG")

                # 将截图添加到报告中
                with open(local_jpg_path, "rb") as image_file:
                    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
                # 将 base64 编码的图片添加到报告中，并包含点击展开功能
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
    # 获取当前时间戳
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    # 分离文件名和扩展名
    base, ext = os.path.splitext(file_path)
    # 构建新的文件名
    new_file_path = f"{base}_{timestamp}{ext}"
    # 重命名文件
    os.rename(file_path, new_file_path)
    return new_file_path

def upload_file_to_network(file_path, network_path):
    # 复制文件到网络路径
    shutil.copy(file_path, network_path)

@pytest.hookimpl(tryfirst=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    # 原始报告文件路径
    original_report_file = "../reports/gallery_all_report.html"
    # 目标网络路径
    network_path = r"\\172.30.1.98\public01\Quality Management\Test Engineering\OS测试资源\Nothing_Gallery\auto_test_report"

    try:
        # 修改报告文件名
        new_report_file = rename_report_file(original_report_file)
        # 上传文件到网络路径
        upload_file_to_network(new_report_file, network_path)
        terminalreporter.write(f"Report has been renamed and uploaded to network path: {network_path}\n")
    except Exception as e:
        terminalreporter.write(f"Failed to process and upload report: {e}\n")