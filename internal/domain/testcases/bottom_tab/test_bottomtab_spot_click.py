from internal.infra.adb.adb_function import ADBClient


def test_bottom_tab_spot_click():
    ADBClient.start_playsee_app().spot_click()
    result = ADBClient.grep_logcat_event_name("bottomtab_spot_click")

    assert result is True, "Test failed: bottomtab_spot_click event not found in logcat"


