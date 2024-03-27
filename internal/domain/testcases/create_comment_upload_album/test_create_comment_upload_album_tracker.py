import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.create_comment_upload_album import CreateCommentUploadAlbum
from internal.infra.validators.validators import Validators


def go_to_create_comment_upload_album():
    ADBClient.start_playsee_app().icon_create_click().icon_album_click()
    return CreateCommentUploadAlbum()


def test_icon_close_click():
    event_name = "icon_close_click"
    go_to_create_comment_upload_album().icon_close_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_title_album_click():
    event_name = "title_album_click"

    go_to_create_comment_upload_album().title_album_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_text_from_profile_show_and_text_from_profile_click():
    event_name = "text_from_profile_show"
    event_name1 = "text_from_profile_click"
    go_to_create_comment_upload_album().text_from_profile_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 5)
    Validators().validate_change_page(result, event_name1)


def test_pic_profile_video_show_and_pic_profile_video_click():
    event_name = "pic_profile_video_show"
    go_to_create_comment_upload_album().text_from_profile_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 5)

    event_name = "pic_profile_video_click"
    CreateCommentUploadAlbum().pic_profile_video_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)
    Validators().validate_change_page(result, event_name)


def test_icon_camera_click():
    event_name = "icon_camera_click"

    go_to_create_comment_upload_album().icon_camera_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_btn_select_click_and_btn_select_show():
    event_name = "btn_select_show"
    event_name1 = "btn_select_click"

    go_to_create_comment_upload_album().first_video_click()
    CreateCommentUploadAlbum().btn_select_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)
    Validators().validate_event_name_in_count(result, event_name,5)
    Validators().validate_change_page(result, event_name1)
