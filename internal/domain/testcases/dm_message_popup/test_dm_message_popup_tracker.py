import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.chatroom import Chatroom
from internal.infra.pages.dm_message_popup import DmMessagePopup
from internal.infra.validators.validators import Validators


def create_a_message_on_dm_and_long_click_message_to_popup():
    ADBClient.start_playsee_app().myprofile_click().icon_dm_click().list_dm_click().bar_message_click()
    Chatroom().bar_message_typing()
    Chatroom().icon_send_click()
    Chatroom().message_longclick()

    return DmMessagePopup()


def test_btn_unsend_click_btn_unsend_show_btn_copy_click_text_cancel_click():
    event_name = "btn_unsend_show"
    create_a_message_on_dm_and_long_click_message_to_popup()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
    event_name = "btn_copy_click"
    DmMessagePopup().btn_copy_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)
    event_name = "text_cancel_click"
    Chatroom().message_longclick()
    DmMessagePopup().text_cancel_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)
    event_name = "btn_unsend_click"
    Chatroom().message_longclick()
    DmMessagePopup().btn_unsend_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)

