import pytest

from internal.infra.adb.adb_function import ADBClient


@pytest.fixture(autouse=True)
def restore_environment():
    ADBClient.stop_playsee_app()
    yield
    ADBClient.stop_playsee_app()