import datetime
import time

import pytest

from internal.infra.adb.adb_function import ADBClient


@pytest.fixture(autouse=True)
def restore_environment():
    ADBClient.stop_playsee_app()
    yield
    ADBClient.stop_playsee_app()
    time.sleep(1)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_protocol(item, nextitem):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    setattr(item.config, 'htmlpath', f'reports/report_{timestamp}.html')
    yield