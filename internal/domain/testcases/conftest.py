import datetime
import time

import pytest
import uiautomator2 as u2
from internal.infra.adb.adb_function import ADBClient


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
