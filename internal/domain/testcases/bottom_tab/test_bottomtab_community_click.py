from internal.infra.adb.adb_function import ADBClient


def test_bottom_tab_community_click():
    ADBClient.start_playsee_app().community_click()
    result = ADBClient.grep_logcat_event_name("bottomtab_community_click")

    assert result is True, "Test failed: bottom_tab_community_click event not found in logcat"


