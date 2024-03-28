import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.searching import Searching
from internal.infra.validators.validators import Validators
from internal.infra.pages.explore import Explore


def go_to_searching():
    ADBClient.start_playsee_app().explore_click().bar_search_click()
    return Searching()


def test_bar_search_click():
    event_name = "bar_search_click"
    go_to_searching().bar_search_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_bar_search_typing():
    event_name = "bar_search_typing"
    go_to_searching().bar_search_typing()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_clear_click():
    event_name = "icon_clear_click"
    go_to_searching().bar_search_typing()
    Searching().icon_clear_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)


def test_icon_back_click():
    event_name = "icon_back_click"
    go_to_searching().list_keyword_click()
    Searching().icon_back_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_tab_spot_click_tab_community_click_tab_user_click_tab_hashtag_click():
    event_name = "tab_community_click"
    go_to_searching().list_keyword_click()
    Searching().tab_community_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)

    event_name = "tab_spot_click"
    Searching().tab_spot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)

    event_name = "tab_user_click"
    Searching().tab_user_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)

    event_name = "tab_hashtag_click"
    Searching().tab_hashtag_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_text_cancel_click():
    event_name = "text_cancel_click"
    go_to_searching().bar_search_typing()
    Searching().text_cancel_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_list_recent_keyword_click():
    event_name = "list_recent_keyword_click"
    content_id = "taipei"
    content_type = "keyword"
    go_to_searching().list_recent_keyword_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page_and_content_id(result, event_name, content_type, content_id)


def test_list_recent_user_click():
    event_name = "list_recent_user_click"
    content_type = "user"
    go_to_searching().list_recent_keyword_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_list_recent_community_click():
    event_name = "list_recent_community_click"
    content_type = "community"
    go_to_searching().list_recent_community_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_list_recent_hashtag_click():
    event_name = "list_recent_hashtag_click"
    content_type = "hashtag"
    content_id = "taipei"
    go_to_searching().list_recent_hashtag_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page_and_content_id(result, event_name, content_type, content_id)


def test_icon_remove_click():
    event_name = "icon_remove_click"
    content_type = "keyword"
    go_to_searching().list_keyword_click()
    Searching().icon_back_click()
    Explore().bar_search_click()
    Searching().icon_remove_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name, content_type)


def test_list_keyword_click():
    event_name = "list_keyword_click"
    content_id = "taipei"
    content_type = "keyword"
    keyword = "taipei"
    go_to_searching().list_keyword_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page_and_content_id_and_key_word(result, event_name, content_type, content_id, keyword)


def test_list_user_click():
    event_name = "list_user_click"
    content_type = "user"
    keyword = "joe"
    go_to_searching().list_user_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page_and_content_id_and_key_word(result, event_name, content_type, None, keyword)


def test_list_community_click():
    event_name = "list_community_click"
    content_type = "community"
    keyword = "dogs"
    go_to_searching().list_community_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_change_page_and_content_id_and_key_word(result, event_name, content_type, None, keyword)
