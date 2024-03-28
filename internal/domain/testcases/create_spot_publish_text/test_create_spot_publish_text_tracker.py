import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.create_spot_publish_text import CreateSpotPublishText
from internal.infra.pages.create_spot_upload_album import CreateSpotUploadAlbum
from internal.infra.validators.validators import Validators


def go_to_create_spot_publish_text():
    ADBClient.start_playsee_app().spot_click().icon_create_click().second_item_select_click()
    CreateSpotUploadAlbum().btn_select_click().textfields_caption_click()

    return CreateSpotPublishText()


def test_icon_back_click():
    event_name = "icon_back_click"
    go_to_create_spot_publish_text().icon_back_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_text_done_click():
    event_name = "text_done_click"
    go_to_create_spot_publish_text().text_done_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_textfields_caption_typing():
    event_name = "textfields_caption_typing"
    go_to_create_spot_publish_text().textfields_caption_typing()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
    event_name = "keyboard_typing"
    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_hashtag_click_btn_hashtag_show_and_btn_hashtag_click_and_btn_hashtag_drag():
    event_name = "icon_hashtag_click"
    go_to_create_spot_publish_text().icon_hashtag_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

    event_name = "btn_hashtag_show"
    Validators().validate_event_name_in_count(result, event_name, 3)

    event_name = "btn_hashtag_drag"
    CreateSpotPublishText().textfields_caption_typing()
    CreateSpotPublishText().btn_hashtag_drag()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
    event_name = "btn_hashtag_click"
    CreateSpotPublishText().btn_hashtag_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_btn_at_user_show_btn_at_user_drag_btn_at_user_click():
    event_name = "btn_at_user_show"
    go_to_create_spot_publish_text().btn_at_user_show()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
    event_name = "btn_at_user_drag"
    CreateSpotPublishText().btn_at_user_drag()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
    event_name = "btn_at_user_click"
    CreateSpotPublishText().btn_at_user_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
