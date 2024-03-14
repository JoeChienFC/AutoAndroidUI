import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.explore import Explore
from internal.infra.validators.validators import Validators


def go_to_explore():
    ADBClient.start_playsee_app().explore_click()
    return Explore()


def test_bar_search_click():
    event_name = "bar_search_click"
    go_to_explore().bar_search_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_pic_spot_l_click():
    event_name = "pic_spot_l_click"
    event_name_1 = "pic_spot_click"
    content_type = "spot"
    go_to_explore().pic_spot_l_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)
    Validators().validate_event_name_content_type_in_count(result, event_name_1, content_type)


def test_pic_spot_s_click():
    event_name = "pic_spot_s_click"
    event_name_1 = "pic_spot_click"
    content_type = "spot"
    go_to_explore().pic_spot_s_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)
    Validators().validate_event_name_content_type_in_count(result, event_name_1, content_type)


def test_pic_community_click():
    event_name = "pic_community_click"
    content_type = 'community'
    go_to_explore().pic_community_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_screen_swipeupanddown():
    event_name = "screen_swipeupanddown"
    go_to_explore().screen_swipeupanddown()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 5)
