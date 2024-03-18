import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.spotfeed import SpotFeed
from internal.infra.pages.shareto_popup import ShareToPopup
from internal.infra.validators.validators import Validators


def test_btn_location_picker_click():
    event_name = "btn_locationpicker_click"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click().location_picker_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_create_click():
    event_name = "icon_create_click"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click().icon_create_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    # 會觸發其他 tracker
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_btn_follow_click_and_btn_unfollow_click():
    event_name = "btn_follow_click"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().btn_follow_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    SpotFeed().btn_unfollow_click()

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)

    event_name = "btn_unfollow_click"
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)
    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_icon_like_click_and_icon_unlike_click():
    event_name = "icon_like_click"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().icon_like_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    SpotFeed().icon_like_click()

    Validators().validate_first_event_name(result, event_name, content_type)

    event_name = "icon_unlike_click"
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)
    Validators().validate_first_event_name(result, event_name, content_type)


def test_icon_comment_click():
    event_name = "icon_comment_click"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().icon_comment_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_share_click():
    event_name = "icon_share_click"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().icon_share_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_more_click():
    event_name = "icon_more_click"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().icon_more_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_pic_headshot_click():
    event_name = "pic_headshot_click"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().pic_headshot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_username_click():
    event_name = "text_username_click"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().text_username_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_location_click():
    event_name = "text_location_click"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().text_location_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_screen_click():
    event_name = "screen_click"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().screen_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name, content_type)


def test_screen_doubleclick():
    event_name = "screen_doubleclick"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().screen_doubleclick()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    SpotFeed().icon_like_click()

    Validators().validate_first_event_name(result, event_name, content_type)


def test_screen_longclick():
    event_name = "screen_longclick"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().screen_longclick()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name, content_type)


def test_screen_swipeleft():
    event_name = "screen_swipeleft"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().screen_swipeleft()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)

def test_screen_swipeupanddown():
    event_name = "screen_swipeupanddown"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().screen_swipeupanddown()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_text_sharecommunity_show():
    event_name = "text_sharecommunity_show"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click().icon_share_click().select_first_community()
    ShareToPopup().share_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name, content_type)


def test_text_sharecommunity_click():
    event_name = "text_sharecommunity_click"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click().icon_share_click().select_first_community()
    ShareToPopup().share_click().text_sharecommunity_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)

def test_text_caption_show():
    event_name = "text_caption_show"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_text_caption_click():
    event_name = "text_caption_click"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click().text_caption_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def btn_collect_click_and_btn_uncollect_click():
    event_name = "btn_collect_click"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click().icon_more_click().btn_collect_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)
    event_name = "btn_uncollect_click"
    SpotFeed().icon_more_click().btn_uncollect_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def btn_download_click():
    event_name = "btn_download_click"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click().icon_more_click().btn_download_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def btn_not_interested_click():
    event_name = "btn_not_interested_click"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click().icon_more_click().btn_not_interested_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def btn_report_click():
    event_name = "btn_report_click"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click().icon_more_click().btn_report_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_content_view_start():
    event_name = "content_view_start"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_content_view_pause():
    event_name = "content_view_pause"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click().icon_more_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)

