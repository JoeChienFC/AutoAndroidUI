import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.community_comment_page import CommunityCommentPage
from internal.infra.pages.community_page import CommunityPage
from internal.infra.pages.communityfeed import CommunityFeed
from internal.infra.pages.create_comment import CreateComment
from internal.infra.validators.validators import Validators


def go_to_community_comment_page_by_self():
    ADBClient.start_playsee_app().text_communityname_click().icon_create_click().textfields_comment_typing_chinese()
    CreateComment().btn_comment_click()
    CommunityPage().icon_back_click()
    CommunityFeed().text_communityname_click()
    CommunityPage().comment_click()
    return CommunityCommentPage()


def delete_community_comment():
    CommunityCommentPage().icon_main_more_click().btn_delete_click()
    CommunityPage().comment_click()
    return CommunityCommentPage()


def test_icon_back_click():
    event_name = "icon_back_click"
    content_type = "community"
    go_to_community_comment_page_by_self().icon_back_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_pic_main_headshot_click():
    event_name = "pic_main_headshot_click"
    content_type = "community_comment"
    go_to_community_comment_page_by_self().pic_main_headshot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_pic_main_username_click():
    event_name = "pic_main_username_click"
    content_type = "community_comment"
    go_to_community_comment_page_by_self().pic_main_username_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_translation_click():
    event_name = "text_translation_click"
    content_type = "community_comment"
    go_to_community_comment_page_by_self().text_translation_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)

