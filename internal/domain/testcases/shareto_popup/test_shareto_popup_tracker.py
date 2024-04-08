import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.delete_popup import DeletePopUp
from internal.infra.pages.shareto_popup import ShareToPopup
from internal.infra.pages.spot_more_popup import SpotMorePopup
from internal.infra.pages.spotfeed import SpotFeed
from internal.infra.pages.system import System
from internal.infra.validators.validators import Validators


def go_to_shareto_popup():
    ADBClient.start_playsee_app().text_communityname_click().btn_share_click()
    return ShareToPopup()


def test_list_community_click_bar_comment_click_bar_comment_typing_btn_share_click():
    event_name = "list_community_click"
    go_to_shareto_popup().list_community_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

    event_name = "bar_comment_click"
    ShareToPopup().bar_comment_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)
    event_name = "bar_comment_typing"
    ShareToPopup().bar_comment_typing()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

    event_name = "btn_share_click"
    ShareToPopup().btn_share_click()
    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_bar_search_click():
    event_name = "bar_search_click"
    go_to_shareto_popup().bar_search_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

    event_name = "bar_search_typing"
    ShareToPopup().bar_search_typing()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

    event_name = "list_result_community_click"
    ShareToPopup().list_result_community_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_screen_swipeupanddown():
    event_name = "screen_swipeupanddown"
    go_to_shareto_popup().screen_swipeupanddown()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_message_click():
    event_name = "icon_message_click"
    go_to_shareto_popup().icon_message_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_change_page(result, event_name)


def test_icon_shareto_click():
    event_name = "icon_shareto_click"
    go_to_shareto_popup().icon_shareto_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_change_page(result, event_name)


def test_icon_copylink_click():
    event_name = "icon_copylink_click"
    go_to_shareto_popup().icon_copylink_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_change_page(result, event_name)
