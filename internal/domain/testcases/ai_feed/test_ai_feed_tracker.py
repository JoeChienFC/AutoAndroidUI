from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.ai_feed import AiFeed
from internal.infra.pages.communityfeed import CommunityFeed
from internal.infra.validators.validators import Validators


def go_to_ai_feed():
    ADBClient.start_playsee_app().ai_click()
    return AiFeed()


def test_bar_message_click():
    event_name = "bar_message_click"
    go_to_ai_feed().bar_message_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_bar_message_typing():
    event_name = "bar_message_typing"
    go_to_ai_feed().bar_message_click()
    AiFeed().bar_message_typing()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_send_click():
    event_name = "icon_send_click"
    go_to_ai_feed().bar_message_click()
    AiFeed().bar_message_typing()
    AiFeed().icon_send_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_pic_spot_show_and_pic_spot_click():
    event_name = "pic_spot_show"
    event_name1 = "icon_send_click"
    content_type = "message"
    go_to_ai_feed().pic_spot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_event_name_content_type_in_count(result, event_name1, content_type)


def test_btn_like_click():
    event_name = "btn_like_click"
    content_type = "message"
    go_to_ai_feed().pic_spot_click()
    AiFeed().btn_like_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_btn_dislike_click():
    event_name = "btn_dislike_click"
    content_type = "message"
    go_to_ai_feed().pic_spot_click()
    AiFeed().btn_dislike_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)