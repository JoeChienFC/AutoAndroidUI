from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.complete_your_profile_page import CompleteYourProfilePage
from internal.infra.pages.new_account_profile_page import NewAccountProfilePage
from internal.infra.validators.validators import Validators


def go_to_complete_your_profile_page_page():
    ADBClient.start_playsee_app()\
        .myprofile_click().\
        icon_menu_click().\
        list_upgradeaccount_click()\
        .btn_upgrade_account_click()

    return CompleteYourProfilePage()


def test_icon_back_click():
    event_name = "icon_back_click"
    go_to_complete_your_profile_page_page().icon_back_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_icon_edit_headshot_click():
    event_name = "pic_edit_headshot_click"
    go_to_complete_your_profile_page_page().icon_edit_headshot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_textfield_change_username_click():
    event_name = "textfield_change_username_click"
    go_to_complete_your_profile_page_page().textfield_change_username_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name)


def test_textfield_password_click():
    event_name = "textfield_password_click"
    go_to_complete_your_profile_page_page().textfield_password_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name)


def test_textfield_confirm_password_click():
    event_name = "textfield_confirm_password_click"
    go_to_complete_your_profile_page_page().textfield_confirm_password_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name)


def test_textfield_email_click():
    event_name = "textfield_email_click"
    go_to_complete_your_profile_page_page().textfield_email_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name)


def test_textfield_birthday_click():
    event_name = "textfield_birthday_click"
    go_to_complete_your_profile_page_page().screen_swipeupanddown()
    CompleteYourProfilePage().textfield_birthday_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name)


def test_textfield_link_click():
    event_name = "textfield_link_click"
    go_to_complete_your_profile_page_page().screen_swipeupanddown()
    CompleteYourProfilePage().textfield_link_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name)


def test_btn_upgrade_click_popup_user_upgraded_to_oa_show_btn_profile_popup_create_ad_cilck():
    event_name = "btn_upgrade_click"
    go_to_complete_your_profile_page_page().btn_upgrade_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)
    event_name = "popup_user_upgraded_to_oa_show"
    Validators().validate_event_name_in_count(result, event_name)

    event_name = "btn_profile_popup_create_ad_cilck"
    NewAccountProfilePage().btn_profile_popup_create_ad_cilck()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)
