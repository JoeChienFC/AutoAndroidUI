import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.create_community_upload_album import CreateCommunityUploadAlbum
from internal.infra.validators.validators import Validators


def go_to_create_community_upload_album():
    ADBClient.start_playsee_app().icon_menu_click().list_create_click().btn_edit_photo_click()
    return CreateCommunityUploadAlbum()


def test_icon_close_click():
    event_name = "icon_close_click"

    go_to_create_community_upload_album().icon_close_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_title_click():
    event_name = "title_click"

    go_to_create_community_upload_album().title_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_screen_swipeupanddown():
    event_name = "screen_swipeupanddown"

    go_to_create_community_upload_album().screen_swipeupanddown()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


