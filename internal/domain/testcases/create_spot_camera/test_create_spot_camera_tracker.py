from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.create_spot_camera import CreateSpotCamera
from internal.infra.pages.create_spot_upload_album import CreateSpotUploadAlbum
from internal.infra.validators.validators import Validators


def go_to_create_spot_camera_page():
    ADBClient.start_playsee_app().spot_click().icon_create_click().icon_camera_click()

    return CreateSpotCamera()


def test_icon_back_click():
    event_name = "icon_back_click"
    go_to_create_spot_camera_page().icon_back_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_icon_timer_click():
    event_name = "icon_timer_click"
    go_to_create_spot_camera_page().icon_timer_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_icon_flash_click():
    event_name = "icon_flash_click"
    go_to_create_spot_camera_page().icon_flash_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_icon_grid_click():
    event_name = "icon_grid_click"
    go_to_create_spot_camera_page().icon_grid_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_icon_filming_guide_click():
    event_name = "icon_filming_guide_click"
    go_to_create_spot_camera_page().icon_filming_guide_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_icon_switch_camera_click():
    event_name = "icon_switch_camera_click"
    go_to_create_spot_camera_page().icon_switch_camera_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_icon_shutter_click():
    event_name = "icon_shutter_click"
    go_to_create_spot_camera_page().icon_shutter_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_icon_album_click():
    event_name = "icon_album_click"
    go_to_create_spot_camera_page().icon_album_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_icon_pause_click():
    event_name = "icon_pause_click"
    go_to_create_spot_camera_page().icon_shutter_click()
    CreateSpotCamera().icon_shutter_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_icon_next_click():
    event_name = "icon_next_click"
    go_to_create_spot_camera_page().icon_shutter_click()
    CreateSpotCamera().icon_shutter_click()
    CreateSpotCamera().icon_next_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_screen_drag():
    event_name = "screen_drag"
    go_to_create_spot_camera_page().screen_drag()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)