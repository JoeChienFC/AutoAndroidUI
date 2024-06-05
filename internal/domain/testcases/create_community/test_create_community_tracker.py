import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.create_community import CreateCommunity
from internal.infra.validators.validators import Validators


def go_to_create_community_page():
    ADBClient.start_playsee_app().icon_menu_click().list_create_click()
    return CreateCommunity()


def test_icon_back_click():
    event_name = "icon_back_click"

    go_to_create_community_page().icon_back_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_btn_edit_photo_click():
    event_name = "btn_edit_photo_click"

    go_to_create_community_page().btn_edit_photo_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_textfields_communityname_click_and_textfields_communityname_typing():
    event_name = "textfields_communityname_click"

    go_to_create_community_page().textfields_communityname_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

    event_name = "textfields_communityname_typing"

    CreateCommunity().textfields_communityname_typing()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_textbar_location_click():
    event_name = "textbar_location_click"

    go_to_create_community_page().textbar_location_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_textfields_description_click_textfields_description_typing():
    event_name = "textfields_description_click"

    go_to_create_community_page().textfields_description_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
    event_name = "textfields_description_typing"

    CreateCommunity().textfields_description_typing()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 5)


def test_btn_create_click():
    event_name = "btn_create_click"
    event_name1 = "publish_community_success"
    content_type = "community"
    go_to_create_community_page().textfields_communityname_click()
    CreateCommunity().textfields_communityname_typing()
    CreateCommunity().btn_create_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)
    Validators().validate_event_name_content_type_in_count(result, event_name1, content_type)
