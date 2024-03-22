import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.dm_list import DmList
from internal.infra.validators.validators import Validators


def go_to_dm_list():
    ADBClient.start_playsee_app().myprofile_click().icon_dm_click()

    return DmList()


def test_icon_back_click():
    event_name = "icon_back_click"
    go_to_dm_list().icon_back_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_icon_addfriend_click():
    event_name = "icon_addfriend_click"
    go_to_dm_list().icon_addfriend_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_list_dm_click():
    event_name = "list_dm_click"
    go_to_dm_list().list_dm_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_pic_headshot_click():
    event_name = "pic_headshot_click"
    go_to_dm_list().pic_headshot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_list_dm_swipeleft():
    event_name = "list_dm_swipeleft"
    go_to_dm_list().list_dm_swipeleft()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_list_dm_longclick():
    event_name = "list_dm_longclick"
    go_to_dm_list().list_dm_longclick()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, 3)