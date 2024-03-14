import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.spot_location_picker import SpotLocationPicker
from internal.infra.validators.validators import Validators


def go_to_spot_location_picker():
    ADBClient.start_playsee_app().spot_click().location_picker_click()
    return SpotLocationPicker()


def test_bar_search_click():
    event_name = "bar_search_click"
    go_to_spot_location_picker().bar_search_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_bar_search_typing():
    event_name = "bar_search_typing"
    go_to_spot_location_picker().bar_search_typing()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_clear_click():
    event_name = "icon_clear_click"
    go_to_spot_location_picker().icon_clear_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_close_click():
    event_name = "icon_close_click"
    go_to_spot_location_picker().icon_close_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_list_recent_click():
    event_name = "list_recent_click"
    go_to_spot_location_picker().list_recent_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 5)


def test_icon_remove_click():
    event_name = "icon_remove_click"
    go_to_spot_location_picker().icon_remove_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_list_spot_click():
    event_name = "list_spot_click"
    content_type = "spot"

    go_to_spot_location_picker().list_spot_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_list_result_spot_click():
    event_name = "list_result_spot_click"
    content_type = "spot"
    position = 0

    go_to_spot_location_picker().list_result_spot_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page_and_position(result, event_name, content_type, position)


def test_text_no_result_show():
    event_name = "text_no_result_show"
    go_to_spot_location_picker().text_no_result_show()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
