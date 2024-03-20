from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.create_spot_publish import CreateSpotPublish
from internal.infra.pages.create_spot_upload_album import CreateSpotUploadAlbum
from internal.infra.validators.validators import Validators


def go_to_create_spot_publish_page():
    ADBClient.start_playsee_app().spot_click().icon_create_click().second_item_select_click()
    CreateSpotUploadAlbum().btn_select_click()
    return CreateSpotPublish()


def test_icon_trim_click():
    event_name = "icon_trim_click"
    go_to_create_spot_publish_page().icon_trim_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_icon_volume_click():
    event_name = "icon_volume_click"
    go_to_create_spot_publish_page().icon_volume_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_icon_download_click():
    event_name = "icon_download_click"
    go_to_create_spot_publish_page().icon_download_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_textfields_caption_click():
    event_name = "textfields_caption_click"
    go_to_create_spot_publish_page().textfields_caption_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_textbar_location_click():
    event_name = "textbar_location_click"
    go_to_create_spot_publish_page().textbar_location_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_btn_post_click():
    event_name = "btn_post_click"
    event_name1 = "publish_spot_success"
    content_type = "spot"
    go_to_create_spot_publish_page().btn_post_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)
    Validators().validate_event_name_content_type_in_count(result, event_name1, content_type)
