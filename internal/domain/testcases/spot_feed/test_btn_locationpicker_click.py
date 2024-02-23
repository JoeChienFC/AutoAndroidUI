from internal.infra.adb.adb_function import ADBClient


def test_btn_location_picker_click():
    ADBClient.start_playsee_app().spot_click().location_picker_click()
    result = ADBClient.grep_logcat_event_name_content_type("btn_locationpicker_click", "spot")

    assert result is True, "Test failed: btn_locationpicker_click event not found in logcat"


