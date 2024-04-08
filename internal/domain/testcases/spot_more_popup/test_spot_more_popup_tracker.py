import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.create_spot_publish import CreateSpotPublish
from internal.infra.pages.create_spot_upload_album import CreateSpotUploadAlbum
from internal.infra.pages.delete_popup import DeletePopUp
from internal.infra.pages.spot_more_popup import SpotMorePopup
from internal.infra.pages.spotfeed import SpotFeed
from internal.infra.pages.system import System
from internal.infra.validators.validators import Validators


def go_to_spot_more_popup():
    ADBClient.start_playsee_app().spot_click().icon_more_click()
    return SpotMorePopup()


def my_profile_create_a_spot_and_go_to_spot_more_popup():
    ADBClient.start_playsee_app().myprofile_click().icon_create_click()
    CreateSpotUploadAlbum().second_item_select_click()
    CreateSpotUploadAlbum().btn_select_click()
    CreateSpotPublish().btn_post_click()
    time.sleep(10)
    SpotFeed().icon_more_click()
    return SpotMorePopup()

def test_btn_collect_click():
    event_name = "btn_collect_click"
    go_to_spot_more_popup().btn_collect_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_btn_download_click():
    event_name = "btn_download_click"
    go_to_spot_more_popup().btn_download_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_btn_notinterested_click():
    event_name = "btn_notinterested_click"
    go_to_spot_more_popup().btn_notinterested_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_btn_report_click():
    event_name = "btn_report_click"
    go_to_spot_more_popup().btn_report_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_text_cancel_click():
    event_name = "text_cancel_click"
    go_to_spot_more_popup().text_cancel_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_btn_edit_click_and_btn_delete_click():
    event_name = "btn_edit_click"
    my_profile_create_a_spot_and_go_to_spot_more_popup().btn_edit_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)
    System().back_click()
    Validators().validate_change_page(result, event_name)

    event_name = "btn_delete_click"
    SpotFeed().icon_more_click()
    SpotMorePopup().btn_delete_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)
    Validators().validate_change_page(result, event_name)
    DeletePopUp().delete_popup()