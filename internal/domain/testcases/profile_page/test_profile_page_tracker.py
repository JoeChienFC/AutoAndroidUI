import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.profile_page import ProfilePage
from internal.infra.validators.validators import Validators


def go_to_profile_page():
    ADBClient.start_playsee_app().myprofile_click()

    return ProfilePage()


def test_title_username_click():
    event_name = "title_username_click"
    content_type = "user"
    go_to_profile_page().title_username_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_dm_click():
    event_name = "icon_dm_click"
    content_type = "user"
    go_to_profile_page().icon_dm_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_notification_click():
    event_name = "icon_notification_click"
    content_type = "user"
    go_to_profile_page().icon_notification_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_menu_click():
    event_name = "icon_menu_click"
    content_type = "user"
    go_to_profile_page().icon_menu_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_create_click():
    event_name = "icon_create_click"
    content_type = "user"
    go_to_profile_page().icon_create_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_pic_l_headshot_click():
    event_name = "pic_l_headshot_click"
    content_type = "user"
    go_to_profile_page().pic_l_headshot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_followers_click():
    event_name = "text_followers_click"
    content_type = "user"
    go_to_profile_page().text_followers_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_following_click():
    event_name = "text_following_click"
    content_type = "user"
    go_to_profile_page().text_following_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_joined_click():
    event_name = "text_joined_click"
    content_type = "user"
    go_to_profile_page().text_joined_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_profile_name_click():
    event_name = "text_profile_name_click"
    content_type = "user"
    go_to_profile_page().text_profile_name_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_bio_click_and_text_bio_show():
    event_name = "text_bio_show"
    event_name1 = "text_bio_click"
    content_type = "user"
    go_to_profile_page().text_bio_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_change_page(result, event_name1, content_type)


def test_btn_editprofile_click():
    event_name = "btn_editprofile_click"
    content_type = "user"
    go_to_profile_page().btn_editprofile_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_btn_share_click():
    event_name = "btn_share_click"
    content_type = "user"
    go_to_profile_page().btn_share_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_btn_contact_click_and_btn_contact_show():
    event_name = "btn_contact_show"
    event_name1 = "btn_contact_click"
    content_type = "user"
    go_to_profile_page().btn_contact_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_change_page(result, event_name1, content_type)


def test_tab_activities_click_and_tab_spots_click():
    event_name = "tab_activities_click"
    content_type = "user"
    go_to_profile_page().tab_activities_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)

    event_name = "tab_spots_click"
    content_type = "user"
    ProfilePage().tab_spots_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_sharespot_show_and_text_sharespot_click():
    event_name = "text_sharespot_show"
    event_name1 = "text_sharespot_click"
    content_type = "user"
    go_to_profile_page().text_sharespot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_change_page(result, event_name1, content_type)


def test_text_url_show_and_text_url_click():
    event_name = "text_url_show"
    event_name1 = "text_url_click"
    content_type = "user"
    go_to_profile_page().text_url_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_change_page(result, event_name1, content_type)