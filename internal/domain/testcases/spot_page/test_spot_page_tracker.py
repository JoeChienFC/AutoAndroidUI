import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.spotfeed import SpotFeed
from internal.infra.pages.myprofile import MyProfile
from internal.infra.pages.shareto_popup import ShareToPopup
from internal.infra.pages.spot_page import SpotPage
from internal.infra.validators.validators import Validators


def go_to_spot_page():
    ADBClient.start_playsee_app().myprofile_click().activities_click()
    MyProfile().comment_click().comment_video_click()
    return SpotPage()


def go_to_explore_spot_page():
    ADBClient.start_playsee_app().explore_click().pic_spot_s_click()
    return SpotPage()

def test_icon_create_click():
    event_name = "icon_create_click"
    content_type = "spot"
    go_to_spot_page().icon_create_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_back_click():
    event_name = "icon_back_click"
    content_type = "spot"
    go_to_spot_page().icon_back_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_title_communityname_show():
    event_name = "title_communityname_show"
    content_type = "spot"
    go_to_spot_page()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_title_communityname_click():
    event_name = "title_communityname_click"
    content_type = "spot"
    go_to_spot_page().title_communityname_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_btn_follow_click_and_btn_unfollow_click():
    event_name = "btn_follow_click"
    content_type = "spot"

    go_to_spot_page().btn_follow_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    SpotPage().btn_unfollow_click()

    Validators().validate_first_event_name(result, event_name, content_type)
    event_name = "btn_unfollow_click"
    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)
    Validators().validate_first_event_name(result, event_name, content_type)

def test_icon_like_click_and_icon_unlike_click():
    event_name = "icon_like_click"
    content_type = "spot"

    go_to_spot_page().icon_like_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    SpotPage().icon_like_click()

    Validators().validate_first_event_name(result, event_name, content_type)
    event_name = "icon_unlike_click"
    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)
    Validators().validate_first_event_name(result, event_name, content_type)

def test_icon_comment_click():
    event_name = "icon_comment_click"
    content_type = "spot"

    go_to_spot_page().icon_comment_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_share_click():
    event_name = "icon_share_click"
    content_type = "spot"

    go_to_spot_page().icon_share_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_more_click():
    event_name = "icon_more_click"
    content_type = "spot"

    go_to_spot_page().icon_more_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_pic_headshot_click():
    event_name = "pic_headshot_click"
    content_type = "spot"

    go_to_spot_page().pic_headshot_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 8)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_username_click():
    event_name = "text_username_click"
    content_type = "spot"

    go_to_spot_page().text_username_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_sharecommunity_show():
    event_name = "text_sharecommunity_show"
    content_type = "spot"
    go_to_spot_page()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_text_sharecommunity_click():
    event_name = "text_sharecommunity_click"
    content_type = "spot"
    go_to_spot_page().text_sharecommunity_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_location_click():
    event_name = "text_location_click"
    content_type = "spot"

    go_to_spot_page().text_location_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_caption_show():
    event_name = "text_caption_show"
    content_type = "spot"
    go_to_spot_page()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_text_caption_click():
    event_name = "text_caption_click"
    content_type = "spot"
    go_to_spot_page().text_caption_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_screen_click():
    event_name = "screen_click"
    content_type = "spot"

    go_to_spot_page().screen_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name, content_type)


def test_screen_doubleclick():
    event_name = "screen_doubleclick"
    content_type = "spot"

    go_to_spot_page().screen_doubleclick()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    SpotPage().icon_like_click()

    Validators().validate_first_event_name(result, event_name, content_type)


def test_screen_longclick():
    event_name = "screen_longclick"
    content_type = "spot"

    go_to_spot_page().screen_longclick()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name, content_type)


def test_screen_swipeleft():
    event_name = "screen_swipeleft"
    content_type = "spot"

    go_to_spot_page().screen_swipeleft()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_screen_swipeupanddown():
    event_name = "screen_swipeupanddown"
    content_type = "spot"

    go_to_explore_spot_page().screen_swipeupanddown()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def btn_collect_click_and_btn_uncollect_click():
    event_name = "btn_collect_click"
    content_type = "spot"
    go_to_spot_page().icon_more_click().btn_collect_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)
    event_name = "btn_uncollect_click"
    go_to_spot_page().icon_more_click().btn_uncollect_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def btn_download_click():
    event_name = "btn_download_click"
    content_type = "spot"
    go_to_spot_page().icon_more_click().btn_download_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def btn_not_interested_click():
    event_name = "btn_not_interested_click"
    content_type = "spot"
    go_to_spot_page().icon_more_click().btn_not_interested_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 7)

    Validators().validate_change_page(result, event_name, content_type)


def btn_report_click():
    event_name = "btn_report_click"
    content_type = "spot"
    go_to_spot_page().icon_more_click().btn_report_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_content_view_start():
    event_name = "content_view_start"
    content_type = "spot"
    go_to_spot_page()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_content_view_pause():
    event_name = "content_view_pause"
    content_type = "spot"
    go_to_spot_page().icon_more_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)

