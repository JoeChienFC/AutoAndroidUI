import base64
import datetime
import os
import subprocess
import time

import pytest
import uiautomator2 as u2
from internal.infra.adb.adb_function import ADBClient
import pytest_html
from pytest_metadata.plugin import metadata_key


def pytest_html_report_title(report):

    report.title = f" Tracker 自動化報告 "


def pytest_configure(config):

    config.stash[metadata_key]["開始時間"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@pytest.fixture(autouse=True)
def restore_environment():
    ADBClient.stop_playsee_app()
    d = u2.connect()
    d.set_fastinput_ime(True)
    # 測試前執行

    yield
    ADBClient.stop_playsee_app()
    time.sleep(1)
    # 測試後執行


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 如果测试失败，执行 adb 命令截取屏幕
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"screenshot_{timestamp}.png"
            local_path = os.path.join(os.getcwd(), screenshot_name)
            try:
                # pytest.set_trace()
                # 使用 adb 截取屏幕并将其保存到本地文件
                subprocess.run(["adb", "shell", "screencap", "-p", f"/sdcard/{screenshot_name}"])
                print(f"Local screenshot path: {local_path}")
                subprocess.run(["adb", "pull", f"/sdcard/{screenshot_name}", local_path], check=True)
                print(f"Screenshot pulled to: {local_path}")
                # 将截图添加到报告中
                with open(local_path, "rb") as image_file:
                    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
                # 将 base64 编码的图片添加到报告中，并包含点击展开功能
                img_html = f"""
                                    <div style="float: right; margin-left: 20px;">
                                        <a href="data:image/png;base64,{image_base64}" target="_blank">
                                            <img src="data:image/png;base64,{image_base64}" style="max-width:300px; max-height:300px;" />
                                        </a>
                                    </div>
                                """
                extra.append(pytest_html.extras.html(img_html))
                # extra.append(
                #     pytest_html.extras.image(image_base64, mime_type='image/png', extension='png', name='screenshot'))
                os.remove(local_path)
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")

        report.extra = extra



