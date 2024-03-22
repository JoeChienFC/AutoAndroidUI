import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.block_popup import BlockPopup
from internal.infra.validators.validators import Validators


def go_to_community_page_more_block_pop_up():
    ADBClient.start_playsee_app().text_communityname_click().comment_icon_more_click().btn_block_click()
    return BlockPopup()


def test_btn_block_click():
    event_name = "btn_block_click"
    go_to_community_page_more_block_pop_up().btn_block_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_btn_cancel_click():
    event_name = "btn_cancel_click"
    go_to_community_page_more_block_pop_up().btn_cancel_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)

