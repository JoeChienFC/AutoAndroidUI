from internal.infra.adb.adb_function import ADBClient
from internal.infra.pages.popUp import PopUp


def test_bottom_tab_my_profile_click():
    ADBClient.start_playsee_app().myprofile_click()
    PopUp().pop_up_13_years_old()
    result = ADBClient.grep_logcat_event_name("bottomtab_myprofile_click")

    assert result is True, "Test failed: bottomtab_myprofile_click event not found in logcat"


