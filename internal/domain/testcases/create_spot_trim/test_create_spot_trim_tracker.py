import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.create_spot_trim import CreateSpotTrim
from internal.infra.pages.create_spot_upload_album import CreateSpotUploadAlbum
from internal.infra.validators.validators import Validators


def go_to_create_spot_trim():
    ADBClient.start_playsee_app().spot_click().icon_create_click().second_item_select_click()
    CreateSpotUploadAlbum().btn_select_click().icon_trim_click()

    return CreateSpotTrim()


def test_text_done_click():
    event_name = "text_done_click"
    go_to_create_spot_trim().text_done_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_icon_play_click():
    event_name = "icon_play_click"
    go_to_create_spot_trim().icon_play_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_fullscreen_click():
    event_name = "icon_fullscreen_click"
    go_to_create_spot_trim().icon_fullscreen_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_bar_videoclips_click():
    event_name = "bar_videoclips_click"
    go_to_create_spot_trim().bar_videoclips_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_bar_videoclips_drag():
    event_name = "bar_videoclips_drag"
    go_to_create_spot_trim().bar_videoclips_drag()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_edit_click():
    event_name = "icon_edit_click"
    go_to_create_spot_trim().icon_edit_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_addclips_click():
    event_name = "icon_addclips_click"
    go_to_create_spot_trim().icon_addclips_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_rotate_click():
    event_name = "icon_rotate_click"
    go_to_create_spot_trim().icon_edit_click()
    CreateSpotTrim().icon_rotate_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_delete_click():
    event_name = "icon_delete_click"
    go_to_create_spot_trim().icon_edit_click()
    CreateSpotTrim().icon_delete_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_split_click():
    event_name = "icon_split_click"
    go_to_create_spot_trim().icon_edit_click()
    CreateSpotTrim().bar_videoclips_drag()
    CreateSpotTrim().icon_split_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
    event_name = "text_changeorder_show"
    Validators().validate_event_name_in_count(result, event_name, 3)
