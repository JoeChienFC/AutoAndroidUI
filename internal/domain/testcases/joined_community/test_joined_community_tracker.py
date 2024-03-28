import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.joined_community import JoinedCommunity
from internal.infra.validators.validators import Validators


def go_to_joined_community():
    ADBClient.start_playsee_app().icon_menu_click().list_joined_click()
    return JoinedCommunity()


def test_bar_search_click():
    event_name = "bar_search_click"
    go_to_joined_community().bar_search_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_bar_search_typing():
    event_name = "bar_search_typing"
    go_to_joined_community().bar_search_typing()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_clear_click():
    event_name = "icon_clear_click"
    go_to_joined_community().bar_search_click()
    JoinedCommunity().bar_search_typing()
    JoinedCommunity().icon_clear_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_list_community_click():
    event_name = "list_community_click"
    content_type = "community"
    go_to_joined_community().list_community_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_list_result_community_click():
    event_name = "list_result_community_click"
    content_type = "community"
    go_to_joined_community().bar_search_click()
    JoinedCommunity().bar_search_typing()
    JoinedCommunity().list_result_community_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_no_result_show():
    event_name = "text_no_result_show"

    go_to_joined_community().text_no_result_show()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

