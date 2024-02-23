from internal.infra.adb.adb_function import ADBClient


def test_bottom_tab_ai_click():
    ADBClient.start_playsee_app().ai_click()
    result = ADBClient.grep_logcat_event_name("bottomtab_ai_click")

    assert result is True, "Test failed: bottomtab_ai_click event not found in logcat"


