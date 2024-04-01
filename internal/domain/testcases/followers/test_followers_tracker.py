import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.followers import Followers
from internal.infra.validators.validators import Validators


def go_to_followers():
    ADBClient.start_playsee_app().myprofile_click().text_followers_click()

    return Followers()


def test_icon_back_click():
    event_name = "icon_back_click"
    go_to_followers().icon_back_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_list_user_click():
    event_name = "list_user_click"
    go_to_followers().list_user_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_text_follow_click_text_following_click():
    event_name = "text_follow_click"
    go_to_followers().text_follow_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
    event_name = "text_following_click"
    Followers().text_following_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_bar_search_click():
    event_name = "bar_search_click"
    go_to_followers().bar_search_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_bar_search_typing():
    event_name = "bar_search_typing"
    go_to_followers().bar_search_click()
    Followers().bar_search_typing()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_clear_click():
    event_name = "icon_clear_click"
    go_to_followers().bar_search_click()
    Followers().bar_search_typing()
    Followers().icon_clear_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_list_result_user_click():
    event_name = "list_result_user_click"
    go_to_followers().list_result_user_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)

