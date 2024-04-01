import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.menu import Menu
from internal.infra.validators.validators import Validators


def go_to_my_profile_menu():
    ADBClient.start_playsee_app().myprofile_click().icon_menu_click()

    return Menu()


def test_icon_back_click():
    event_name = "icon_back_click"
    go_to_my_profile_menu().icon_back_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_icon_moon_s_click_icon_moon_f_click():
    event_name = "icon_moon_s_click"
    go_to_my_profile_menu().icon_moon_s_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
    event_name = "icon_moon_f_click"
    Menu().icon_moon_s_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_list_account_click():
    event_name = "list_account_click"
    go_to_my_profile_menu().list_account_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_list_collected_click():
    event_name = "list_collected_click"
    go_to_my_profile_menu().list_collected_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_list_liked_click():
    event_name = "list_liked_click"
    go_to_my_profile_menu().list_liked_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_list_comments_click():
    event_name = "list_comments_click"
    go_to_my_profile_menu().list_comments_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_list_addfriends_click():
    event_name = "list_addfriends_click"
    go_to_my_profile_menu().list_addfriends_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_list_switchaccount_click():
    event_name = "list_switchaccount_click"
    go_to_my_profile_menu().list_switchaccount_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_list_settings_click():
    event_name = "list_settings_click"
    go_to_my_profile_menu().list_settings_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)
