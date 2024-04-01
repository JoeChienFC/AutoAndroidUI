import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.spot_more_popup import SpotMorePopup
from internal.infra.validators.validators import Validators


def go_to_spot_more_popup():
    ADBClient.start_playsee_app().spot_click().icon_more_click()
    return SpotMorePopup()


def test_btn_collect_click():
    event_name = "btn_collect_click"
    go_to_spot_more_popup().btn_collect_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_btn_download_click():
    event_name = "btn_download_click"
    go_to_spot_more_popup().btn_download_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_btn_notinterested_click():
    event_name = "btn_notinterested_click"
    go_to_spot_more_popup().btn_notinterested_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_btn_report_click():
    event_name = "btn_report_click"
    go_to_spot_more_popup().btn_report_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_text_cancel_click():
    event_name = "text_cancel_click"
    go_to_spot_more_popup().text_cancel_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 5)


def test_icon_remove_click():
    event_name = "icon_remove_click"
    go_to_spot_more_popup().icon_remove_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_list_spot_click():
    event_name = "list_spot_click"
    content_type = "spot"

    go_to_spot_more_popup().list_spot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_list_result_spot_click():
    event_name = "list_result_spot_click"
    content_type = "spot"
    position = 0

    go_to_spot_more_popup().list_result_spot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page_and_position(result, event_name, content_type, position)


def test_text_no_result_show():
    event_name = "text_no_result_show"
    go_to_spot_more_popup().text_no_result_show()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
