import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.search_community import SearchCommunity
from internal.infra.pages.searching import Searching
from internal.infra.validators.validators import Validators
from internal.infra.pages.explore import Explore


def go_to_search_community():
    ADBClient.start_playsee_app().explore_click().bar_search_click()
    Searching().list_keyword_click()
    Searching().tab_community_click()
    time.sleep(10)
    return SearchCommunity()


def test_text_communityname_click():
    event_name = "text_communityname_click"
    content_type = "community"
    go_to_search_community().text_communityname_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_pic_headshot_click():
    event_name = "pic_headshot_click"
    content_type = "community_comment"
    go_to_search_community().pic_headshot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_username_click():
    event_name = "text_username_click"
    content_type = "community_comment"
    go_to_search_community().text_username_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_comment_text_click():
    event_name = "comment_text_click"
    content_type = "community_comment"
    go_to_search_community().comment_text_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_comment_click():
    event_name = "icon_comment_click"
    content_type = "community_comment"
    go_to_search_community().icon_comment_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_share_click():
    event_name = "icon_share_click"
    content_type = "community_comment"
    go_to_search_community().icon_share_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_like_click():
    event_name = "icon_like_click"
    content_type = "community_comment"
    go_to_search_community().icon_like_click()
    SearchCommunity().icon_like_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_icon_more_click():
    event_name = "icon_more_click"
    content_type = "community_comment"
    go_to_search_community().icon_more_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)
