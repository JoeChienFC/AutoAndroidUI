import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.communityfeed import CommunityFeed
from internal.infra.validators.validators import Validators


def test_btn_location_picker_click():
    event_name = "btn_locationpicker_click"
    ADBClient.start_playsee_app().btn_locationpicker_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_icon_menu_click():
    event_name = "icon_menu_click"
    ADBClient.start_playsee_app().icon_menu_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


# def test_icon_create_click():
#     event_name = "icon_create_click"
#     ADBClient.start_playsee_app().icon_create_click()
#
#     result = BigQueryFunction().fetch_user_operation_tracker()
#     BigQueryFunction().display_query_result(result, 5)
#
#     Validators().validate_change_page(result, event_name)


def test_text_communityname_click():
    event_name = "text_communityname_click"
    content_type = "community"

    ADBClient.start_playsee_app().text_communityname_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_change_page(result, event_name, content_type)


def test_pic_headshot_click():
    event_name = "pic_headshot_click"
    content_type = "community_comment"

    ADBClient.start_playsee_app().pic_headshot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_username_click():
    event_name = "text_username_click"
    content_type = "community_comment"

    ADBClient.start_playsee_app().text_username_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_change_page(result, event_name, content_type)


def test_comment_text_click():
    event_name = "comment_text_click"
    content_type = "community_comment"

    ADBClient.start_playsee_app().comment_text_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_comment_media_show():
    event_name = "comment_media_show"
    content_type = "community_comment"

    ADBClient.start_playsee_app()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_comment_media_click():
    event_name = "comment_media_click"
    content_type = "community_comment"

    ADBClient.start_playsee_app().comment_media_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_comment_click():
    event_name = "icon_comment_click"
    content_type = "community_comment"

    ADBClient.start_playsee_app().icon_comment_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_share_click():
    event_name = "icon_share_click"
    content_type = "community_comment"

    ADBClient.start_playsee_app().icon_share_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_like_click_icon_unlike_click():
    event_name = "icon_like_click"
    event_name2 = "icon_unlike_click"
    content_type = "community_comment"

    ADBClient.start_playsee_app().icon_unlike_click()

    result1 = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result1, 5)

    CommunityFeed().icon_like_click()

    result2 = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result2, 5)

    Validators().validate_first_event_name(result1, event_name, content_type)
    Validators().validate_first_event_name(result2, event_name2, content_type)


def test_icon_save_click_icon_unsave_click():
    event_name = "icon_save_click"
    event_name2 = "icon_unsave_click"
    content_type = "community_comment"

    ADBClient.start_playsee_app().icon_unsave_click()

    result1 = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result1, 5)

    CommunityFeed().icon_save_click()

    result2 = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result2, 5)

    Validators().validate_first_event_name(result1, event_name, content_type)
    Validators().validate_first_event_name(result2, event_name2, content_type)


def test_icon_more_click():
    event_name = "icon_more_click"
    content_type = "community_comment"

    ADBClient.start_playsee_app().icon_more_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_screen_swipeupanddown():
    event_name = "screen_swipeupanddown"

    ADBClient.start_playsee_app().screen_swipeupanddown()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 5)


def test_comment_appear():
    event_name = "comment_appear"
    ADBClient.start_playsee_app()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 10)


def test_comment_disappear():
    event_name = "comment_disappear"
    ADBClient.start_playsee_app().screen_swipeupanddown()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 10)
