import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.community_comment_page import CommunityCommentPage
from internal.infra.pages.communityfeed import CommunityFeed
from internal.infra.validators.validators import Validators


def go_to_community_comment_page():
    ADBClient.start_playsee_app().text_communityname_click().comment_click()
    return CommunityCommentPage()


def test_icon_back_click():
    event_name = "icon_back_click"
    content_type = "community"
    go_to_community_comment_page().icon_back_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_pic_main_headshot_click():
    event_name = "pic_main_headshot_click"
    content_type = "community_comment"
    go_to_community_comment_page().pic_main_headshot_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_pic_main_username_click():
    event_name = "pic_main_username_click"
    content_type = "community_comment"
    go_to_community_comment_page().pic_main_username_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_translation_click():
    event_name = "text_translation_click"
    content_type = "community_comment"
    go_to_community_comment_page().text_translation_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)

