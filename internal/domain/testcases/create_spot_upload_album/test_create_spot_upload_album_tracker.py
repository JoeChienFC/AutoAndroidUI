from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.create_spot_upload_album import CreateSpotUploadAlbum
from internal.infra.pages.spotfeed import SpotFeed
from internal.infra.pages.myprofile import MyProfile
from internal.infra.pages.shareto_popup import ShareToPopup
from internal.infra.pages.spot_page import SpotPage
from internal.infra.validators.validators import Validators


def go_to_create_spot_upload_album_page():
    ADBClient.start_playsee_app().spot_click().icon_create_click()

    return CreateSpotUploadAlbum()


def test_icon_create_click():
    event_name = "icon_close_click"
    go_to_create_spot_upload_album_page().icon_close_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_title_album_click():
    event_name = "title_album_click"
    go_to_create_spot_upload_album_page().title_album_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_camera_click():
    event_name = "icon_camera_click"
    go_to_create_spot_upload_album_page().icon_camera_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_pic_video_click():
    event_name = "pic_video_click"
    go_to_create_spot_upload_album_page().pic_video_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_icon_select_click():
    event_name = "icon_select_click"
    go_to_create_spot_upload_album_page().icon_select_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)
    event_name = "btn_select_click"
    CreateSpotUploadAlbum().btn_select_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)



