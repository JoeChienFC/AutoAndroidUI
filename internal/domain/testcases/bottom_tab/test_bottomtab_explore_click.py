from internal.infra.adb.adb_function import ADBClient


def test_bottom_tab_explore_click():
    ADBClient.start_playsee_app().explore_click()
    result = ADBClient.grep_logcat_event_name("bottomtab_explore_click")

    assert result is True, "Test failed: bottomtab_explore_click event not found in logcat"


