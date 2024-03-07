import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.community_page import CommunityPage
from internal.infra.pages.create_comment import CreateComment
from internal.infra.pages.spot_page import SpotPage
from internal.infra.validators.validators import Validators


def go_to_community_page():
    ADBClient.start_playsee_app().text_communityname_click()
    return CommunityPage()


def create_a_location_comment():
    CommunityPage().icon_create_click()
    CreateComment().textfields_comment_typing()
    CreateComment().icon_location_pin_click().text_done_click()
    CreateComment().btn_comment_click()
    return CommunityPage()

def test_icon_back_click():
    event_name = "icon_back_click"
    content_type = "community"
    go_to_community_page().icon_back_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_more_click():
    event_name = "icon_more_click"
    content_type = "community"

    go_to_community_page().icon_more_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_communitylocation_click():
    event_name = "text_communitylocation_click"
    content_type = "community"

    go_to_community_page().text_communitylocation_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name, content_type)


def test_text_members_click():
    event_name = "text_members_click"
    content_type = "community"

    go_to_community_page().text_members_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name, content_type)


def test_btn_join_click():
    event_name = "btn_join_click"
    content_type = "community"

    go_to_community_page().btn_join_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    CommunityPage().btn_unjoin_click()
    Validators().validate_first_event_name(result, event_name, content_type)


def test_btn_share_click():
    event_name = "btn_share_click"
    content_type = "community"

    go_to_community_page().btn_share_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_tab_activities_click():
    event_name = "tab_activities_click"
    content_type = "community"

    go_to_community_page().tab_activities_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name, content_type)


def test_tab_spots_click():
    event_name = "tab_spots_click"
    content_type = "community"

    go_to_community_page().tab_spots_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_create_click():
    event_name = "icon_create_click"
    content_type = "community"
    go_to_community_page().icon_create_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_screen_swipeupanddown():
    event_name = "screen_swipeupanddown"
    content_type = "community"

    go_to_community_page().screen_swipeupanddown()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_content_view_load():
    event_name = "content_view_load"
    content_type = "community"

    go_to_community_page().screen_swipeupanddown()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_pic_headshot_click():
    event_name = "pic_headshot_click"
    content_type = "community_comment"

    go_to_community_page().pic_headshot_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 8)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_username_click():
    event_name = "text_username_click"
    content_type = "community_comment"

    go_to_community_page().text_username_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_location_show():
    event_name = "text_location_show"
    content_type = "community_comment"

    go_to_community_page()
    create_a_location_comment()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_text_location_click():
    event_name = "text_location_click"
    content_type = "community_comment"

    go_to_community_page()
    create_a_location_comment().text_location_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


    # ---------
def test_title_communityname_show():
    event_name = "title_communityname_show"
    content_type = "community_comment"
    go_to_community_page()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_title_communityname_click():
    event_name = "title_communityname_click"
    content_type = "community_comment"
    go_to_community_page().title_communityname_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_btn_follow_click():
    event_name = "btn_follow_click"
    content_type = "community_comment"

    go_to_community_page().btn_follow_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    SpotPage().btn_unfollow_click()

    Validators().validate_first_event_name(result, event_name, content_type)


def test_icon_like_click():
    event_name = "icon_like_click"
    content_type = "community_comment"

    go_to_community_page().icon_like_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    SpotPage().icon_like_click()

    Validators().validate_first_event_name(result, event_name, content_type)


def test_icon_comment_click():
    event_name = "icon_comment_click"
    content_type = "community_comment"

    go_to_community_page().icon_comment_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_share_click():
    event_name = "icon_share_click"
    content_type = "community_comment"

    go_to_community_page().icon_share_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_sharecommunity_show():
    event_name = "text_sharecommunity_show"
    content_type = "community_comment"
    go_to_community_page()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_text_sharecommunity_click():
    event_name = "text_sharecommunity_click"
    content_type = "community_comment"
    go_to_community_page().text_sharecommunity_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_caption_show():
    event_name = "text_caption_show"
    content_type = "community_comment"
    go_to_community_page()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_text_caption_click():
    event_name = "text_caption_click"
    content_type = "community_comment"
    go_to_community_page().text_caption_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_screen_click():
    event_name = "screen_click"
    content_type = "community_comment"

    go_to_community_page().screen_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name, content_type)


def test_screen_doubleclick():
    event_name = "screen_doubleclick"
    content_type = "community_comment"

    go_to_community_page().screen_doubleclick()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    SpotPage().icon_like_click()

    Validators().validate_first_event_name(result, event_name, content_type)


def test_screen_longclick():
    event_name = "screen_longclick"
    content_type = "community_comment"

    go_to_community_page().screen_longclick()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name, content_type)


def test_screen_swipeleft():
    event_name = "screen_swipeleft"
    content_type = "community_comment"

    go_to_community_page().screen_swipeleft()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)




