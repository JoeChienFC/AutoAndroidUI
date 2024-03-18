import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.community_location_picker import CommunityLocationPicker
from internal.infra.validators.validators import Validators


def go_to_community_location_picker():
    ADBClient.start_playsee_app().btn_locationpicker_click()
    return CommunityLocationPicker()


def test_bar_search_click():
    event_name = "bar_search_click"
    go_to_community_location_picker().bar_search_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_bar_search_typing():
    event_name = "bar_search_typing"
    go_to_community_location_picker().bar_search_typing()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_clear_click():
    event_name = "icon_clear_click"
    go_to_community_location_picker().icon_clear_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_close_click():
    event_name = "icon_close_click"
    go_to_community_location_picker().icon_close_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_list_recent_click():
    event_name = "list_recent_click"
    go_to_community_location_picker().list_recent_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_change_page(result, event_name)


def test_icon_remove_click():
    event_name = "icon_remove_click"
    go_to_community_location_picker().icon_remove_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_list_spot_click():
    event_name = "list_community_click"
    content_type = "community"
    position = 1

    go_to_community_location_picker().list_community_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    CommunityLocationPicker().icon_remove_click()

    Validators().validate_change_page_and_position(result, event_name, content_type, position)


def test_list_result_community_click():
    event_name = "list_result_community_click"
    content_type = "community"
    position = 0

    go_to_community_location_picker().list_result_community_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page_and_position(result, event_name, content_type, position)


def test_text_no_result_show():
    event_name = "text_no_result_show"
    go_to_community_location_picker().text_no_result_show()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
