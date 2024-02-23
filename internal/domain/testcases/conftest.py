import pytest

from internal.infra.adb.adb_function import ADBClient


@pytest.fixture(autouse=True)
def restore_environment():
    ADBClient.stop_playsee_app()
    yield
    ADBClient.stop_playsee_app()


# 在 conftest.py 或者你的測試模塊中

def pytest_runtest_protocol(item, nextitem):
    # 檢查測試是否失敗
    if nextitem is None and item.config.option.runxfail:
        failed_tests = item.config.hook.pytest_runtest_protocol(item=item, nextitem=nextitem)
        if failed_tests:
            # 在這裡執行額外的操作
            print("=======================")
            print("測試失敗，執行額外的操作...")