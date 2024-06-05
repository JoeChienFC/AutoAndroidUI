import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.community_page import CommunityPage
from internal.infra.pages.create_comment import CreateComment
from internal.infra.pages.create_comment_upload_album import CreateCommentUploadAlbum
from internal.infra.pages.create_spot_publish import CreateSpotPublish
from internal.infra.pages.system import System
from internal.infra.validators.validators import Validators
import pytest


def go_to_create_comment():
    ADBClient.start_playsee_app().text_communityname_click().btn_join_click()
    CommunityPage().icon_create_click()
    return CreateComment()


def test_icon_close_click():
    event_name = "icon_close_click"
    go_to_create_comment().icon_close_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)
    CommunityPage().btn_unjoin_click()
    CommunityPage().btn_leave_community_popup_leave_this_community_click()
    Validators().validate_change_page(result, event_name)


# def test_btn_community_click():
#     event_name = "btn_community_click"
#     go_to_create_comment().btn_community_click()
#
#     result = BigQueryFunction().fetch_user_operation_tracker()
#     BigQueryFunction().display_query_result(result, 5)
#     CommunityPage().btn_unjoin_click()
#     CommunityPage().btn_leave_community_popup_leave_this_community_click()
#     Validators().validate_change_page(result, event_name)


def test_textfields_comment_click():
    event_name = "textfields_comment_click"
    go_to_create_comment()
    System().back_click()
    CreateComment().textfields_comment_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)
    CreateComment().icon_close_click()
    CommunityPage().btn_unjoin_click()
    CommunityPage().btn_leave_community_popup_leave_this_community_click()
    Validators().validate_event_name_in_count(result, event_name)


def test_textfields_comment_typing_and_btn_comment_click_and_publish_comment_success():
    event_name = "textfields_comment_typing"
    go_to_create_comment().textfields_comment_typing()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

    event_name = "btn_comment_click"
    content_type = "community"
    event_name_2 = "publish_comment_success"
    content_type_2 = "community_comment"

    CreateComment().btn_comment_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)
    Validators().validate_change_page(result, event_name, content_type)

    CommunityPage().btn_unjoin_click()
    CommunityPage().btn_leave_community_popup_leave_this_community_click()

    Validators().validate_event_name_content_type_in_count(result, event_name_2, content_type_2)


def test_icon_album_click():
    event_name = "icon_album_click"
    go_to_create_comment().icon_album_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)
    System().back_click()
    CreateComment().icon_close_click()
    CommunityPage().btn_unjoin_click()
    CommunityPage().btn_leave_community_popup_leave_this_community_click()
    Validators().validate_change_page(result, event_name)


def test_icon_location_pin_click():
    event_name = "icon_location_pin_click"
    go_to_create_comment().icon_location_pin_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)
    System().back_click()
    CreateComment().icon_close_click()
    CommunityPage().btn_unjoin_click()
    CommunityPage().btn_leave_community_popup_leave_this_community_click()
    Validators().validate_change_page(result, event_name)


def test_btn_at_user_show_and_btn_at_user_drag_and_btn_at_user_click():
    event_name = "btn_at_user_show"
    go_to_create_comment().textfields_comment_typing_at_user()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)
    event_name = "btn_at_user_drag"
    CreateComment().btn_at_user_drag()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)
    event_name = "btn_at_user_click"
    CreateComment().btn_at_user_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_btn_hashtag_show_and_btn_hashtag_drag_and_btn_hashtag_click():
    event_name = "btn_hashtag_show"
    go_to_create_comment().textfields_comment_typing_hashtag()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)
    event_name = "btn_hashtag_drag"
    CreateComment().btn_hashtag_drag()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)
    event_name = "btn_hashtag_click"
    CreateComment().btn_hashtag_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_pic_preview_show_and_btn_pic_preview_drag_and_icon_preview_close_click_text_location_show_icon_location_close_click():
    event_name = "pic_preview_show"
    event_name1 = 'text_location_show'
    go_to_create_comment().icon_album_click()
    CreateCommentUploadAlbum().change_pic_album()
    CreateCommentUploadAlbum().select_5_pic_or_video()
    CreateCommentUploadAlbum().btn_select_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 5)
    Validators().validate_event_name_in_count(result, event_name1, 5)

    event_name = "pic_preview_drag"
    CreateComment().pic_preview_drag()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)

    event_name = "icon_location_close_click"
    CreateCommentUploadAlbum().icon_location_close_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

    event_name = "icon_preview_close_click"
    CreateComment().icon_preview_close_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name)


def test_pic_video_preview_show_icon_video_preview_close_click():
    event_name = "pic_video_preview_show"
    go_to_create_comment().icon_album_click()
    CreateCommentUploadAlbum().change_video_album()
    CreateCommentUploadAlbum().first_video_click()
    CreateCommentUploadAlbum().btn_select_click()
    CreateSpotPublish().btn_post_click_comment()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

    event_name = "icon_video_preview_close_click"
    CreateComment().icon_preview_close_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_pic_url_preview_show_and_icon_url_preview_close_click():
    event_name = "pic_url_preview_show"
    go_to_create_comment().comment_url_typing()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

    event_name = "icon_url_preview_close_click"
    CreateComment().icon_url_preview_close_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_btn_add_show_and_btn_add_click():
    event_name = "btn_add_show"

    go_to_create_comment().icon_album_click()
    CreateCommentUploadAlbum().change_pic_album()
    CreateCommentUploadAlbum().first_video_click()
    CreateCommentUploadAlbum().btn_select_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

    event_name = "btn_add_click"
    CreateComment().btn_add_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)
