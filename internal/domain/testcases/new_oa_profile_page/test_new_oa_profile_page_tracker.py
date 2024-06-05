import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.new_account_profile_page import NewAccountProfilePage
from internal.infra.validators.validators import Validators


def go_to_profile_page():
    ADBClient.start_playsee_app().myprofile_click()

    return NewAccountProfilePage()


def test_card_addbio_click():
    event_name = "card_addbio_click"
    content_type = "user"
    go_to_profile_page().card_addbio_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_no_comment_show():
    event_name = "text_no_comment_show"
    content_type = "user"
    go_to_profile_page().tab_activities_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_text_sharecomment_click_text_sharecomment_show():
    event_name = "text_sharecomment_show"
    event_name1 = "text_sharecomment_click"
    content_type = "user"
    go_to_profile_page().tab_activities_click()
    NewAccountProfilePage().text_sharecomment_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_change_page(result, event_name1, content_type)