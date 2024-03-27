import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.create_community_cover_reposition import CreateCommunityCoverReposition
from internal.infra.validators.validators import Validators


def go_to_create_community_cover_reposition():
    ADBClient.start_playsee_app().icon_menu_click().list_create_click().btn_edit_photo_click().select_photo()
    return CreateCommunityCoverReposition()


def test_icon_back_click():
    event_name = "icon_back_click"

    go_to_create_community_cover_reposition().icon_back_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_text_save_click():
    event_name = "text_save_click"

    go_to_create_community_cover_reposition().text_save_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_screen_drag():
    event_name = "screen_drag"

    go_to_create_community_cover_reposition().screen_drag()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


