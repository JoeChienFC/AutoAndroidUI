import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.comment_more_popup import CommentMorePopup
from internal.infra.validators.validators import Validators


def go_to_community_page_more_pop_up():
    ADBClient.start_playsee_app().text_communityname_click().comment_icon_more_click()
    return CommentMorePopup()


# def test_btn_replyto_click():
#     event_name = "btn_replyto_click"
#     go_to_community_page_more_pop_up().btn_replyto_click()
#
#     result = BigQueryFunction().fetch_user_operation_tracker()
#     BigQueryFunction().display_query_result(result, 5)
#
#     Validators().validate_change_page(result, event_name)


def test_btn_share_click():
    event_name = "btn_share_click"
    go_to_community_page_more_pop_up().btn_share_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_btn_block_click():
    event_name = "btn_block_click"
    go_to_community_page_more_pop_up().btn_block_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_text_cancel_click():
    event_name = "text_cancel_click"
    go_to_community_page_more_pop_up().text_cancel_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_text_cancel_closed_outside_click():
    event_name = "text_cancel_click"
    go_to_community_page_more_pop_up().text_cancel_closed_outside_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)
