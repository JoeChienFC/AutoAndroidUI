import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.bottom_tab import BottomTab
from internal.infra.pages.community_page import CommunityPage
from internal.infra.pages.create_comment import CreateComment
from internal.infra.pages.create_comment_upload_album import CreateCommentUploadAlbum
from internal.infra.pages.profile_page_activities import ProfilePageActivities
from internal.infra.pages.shareto_popup import ShareToPopup
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


def create_a_media_comment():
    CommunityPage().icon_create_click()
    CreateComment().icon_album_click()
    CreateCommentUploadAlbum().select_video_from_profile_click()
    CreateComment().btn_comment_click()
    return CommunityPage()


def test_icon_back_click():
    event_name = "icon_back_click"
    content_type = "community"
    go_to_community_page().icon_back_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_more_click():
    event_name = "icon_more_click"
    content_type = "community"

    go_to_community_page().icon_more_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_communitylocation_click():
    event_name = "text_communitylocation_click"
    content_type = "community"

    go_to_community_page().text_communitylocation_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_members_click():
    event_name = "text_members_click"
    content_type = "community"

    go_to_community_page().text_members_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_btn_join_click_icon_create_click_popup_leave_community_show_btn_leave_community_popup_cancel_click_btn_leave_community_popup_leave_this_community_click():
    event_name = "btn_join_click"
    event_name1 = "popup_leave_community_show"
    event_name2 = "btn_leave_community_popup_cancel_click"
    event_name3 = "btn_leave_community_popup_leave_this_community_click"
    event_name4 = "icon_create_click"
    content_type = "community"

    go_to_community_page().btn_join_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)

    CommunityPage().icon_create_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name4, 10)

    CreateComment().icon_close_click()
    CommunityPage().btn_unjoin_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name1, 10)

    CommunityPage().btn_leave_community_popup_cancel_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name2, 10)

    CommunityPage().btn_unjoin_click()
    CommunityPage().btn_leave_community_popup_leave_this_community_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name3, 10)


def test_btn_share_click():
    event_name = "btn_share_click"
    content_type = "community"

    go_to_community_page().btn_share_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_tab_activities_click():
    event_name = "tab_activities_click"
    content_type = "community"

    go_to_community_page().tab_activities_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_tab_spots_click():
    event_name = "tab_spots_click"
    content_type = "community"

    go_to_community_page().tab_spots_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_screen_swipeupanddown():
    event_name = "screen_swipeupanddown"
    content_type = "community"

    go_to_community_page().screen_swipeupanddown()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_pic_headshot_click():
    event_name = "pic_headshot_click"
    content_type = "community_comment"

    go_to_community_page().pic_headshot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 8)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_username_click():
    event_name = "text_username_click"
    content_type = "community_comment"

    go_to_community_page().text_username_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_location_show_text_location_click():
    event_name = "text_location_show"
    event_name1 = "text_location_click"
    content_type = "community_comment"

    go_to_community_page().text_location_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_change_page(result, event_name1, content_type)


def test_comment_appear_comment_disappear():
    event_name = "comment_appear"
    event_name1 = "comment_disappear"
    content_type = "community_comment"

    go_to_community_page().screen_swipeupanddown()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_event_name_content_type_in_count(result, event_name1, content_type)


def test_comment_text_click():
    event_name = "comment_text_click"
    content_type = "community_comment"

    go_to_community_page().comment_text_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_comment_media_show_comment_media_click():
    event_name = "comment_media_show"
    event_name1 = "comment_media_click"
    content_type = "community_comment"

    go_to_community_page().comment_media_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_change_page(result, event_name1, content_type)


def test_icon_comment_click():
    event_name = "icon_comment_click"
    content_type = "community_comment"

    go_to_community_page().icon_comment_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_share_click():
    event_name = "icon_share_click"
    content_type = "community_comment"

    go_to_community_page().icon_share_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_save_click_icon_unsave_click():
    event_name = "icon_save_click"
    event_name1 = "icon_unsave_click"
    content_type = "community_comment"

    go_to_community_page().icon_save_click()
    CommunityPage().icon_unsave_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_event_name_content_type_in_count(result, event_name1, content_type)


def test_icon_like_click():
    event_name = "icon_like_click"
    event_name1 = "icon_unlike_click"
    content_type = "community_comment"

    go_to_community_page().icon_like_click()
    CommunityPage().icon_unlike_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_event_name_content_type_in_count(result, event_name1, content_type)


def test_comment_icon_more_click():
    event_name = "icon_more_click"
    content_type = "community_comment"

    go_to_community_page().screen_swipeupanddown()
    CommunityPage().icon_more_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_pic_spot_click():
    event_name = "pic_spot_click"
    content_type = "spot"

    go_to_community_page().tab_spots_click()
    CommunityPage().pic_spot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)

