import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.community_feed_dropdown_menu import CommunityFeedDropdownMenu
from internal.infra.validators.validators import Validators


def go_to_community_feed_dropdown_menu_page():
    ADBClient.start_playsee_app().icon_menu_click()
    return CommunityFeedDropdownMenu()


def test_list_create_click():
    event_name = "list_create_click"

    go_to_community_feed_dropdown_menu_page().list_create_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_list_joined_click():
    event_name = "list_joined_click"

    go_to_community_feed_dropdown_menu_page().list_joined_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)

