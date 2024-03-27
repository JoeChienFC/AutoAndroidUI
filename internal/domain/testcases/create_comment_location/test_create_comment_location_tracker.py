import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.create_comment_location import CreateCommentLocation
from internal.infra.pages.create_community_location import CreateCommunityLocation
from internal.infra.validators.validators import Validators


def go_to_create_comment_location():
    ADBClient.start_playsee_app().icon_create_click().icon_location_pin_click()
    return CreateCommentLocation()


def test_text_done_click():
    event_name = "text_done_click"
    go_to_create_comment_location().text_done_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_bar_search_click():
    event_name = "bar_search_click"
    go_to_create_comment_location().bar_search_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_bar_search_typing():
    event_name = "bar_search_typing"
    go_to_create_comment_location().bar_search_typing()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_clear_click():
    event_name = "icon_clear_click"
    go_to_create_comment_location().bar_search_click()
    CreateCommunityLocation().bar_search_typing()
    CreateCommunityLocation().icon_clear_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_list_location_click():
    event_name = "list_location_click"
    go_to_create_comment_location().list_location_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_list_result_location_click():
    event_name = "list_result_location_click"
    go_to_create_comment_location().bar_search_click()
    CreateCommunityLocation().bar_search_typing()
    CreateCommunityLocation().list_result_location_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_text_no_result_show():
    event_name = "text_no_result_show"

    go_to_create_comment_location().text_no_result_show()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

