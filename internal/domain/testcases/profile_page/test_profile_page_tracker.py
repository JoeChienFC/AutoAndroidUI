import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.profile_page import ProfilePage
from internal.infra.validators.validators import Validators


def go_to_profile_page():
    ADBClient.start_playsee_app().myprofile_click()

    return ProfilePage()


def test_title_username_click():
    event_name = "title_username_click"
    content_type = "user"
    go_to_profile_page().title_username_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_dm_click():
    event_name = "icon_dm_click"
    content_type = "user"
    go_to_profile_page().icon_dm_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_menu_click():
    event_name = "icon_menu_click"
    content_type = "user"
    go_to_profile_page().icon_menu_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_create_click():
    event_name = "icon_create_click"
    content_type = "user"
    go_to_profile_page().icon_create_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_pic_l_headshot_click():
    event_name = "pic_l_headshot_click"
    content_type = "user"
    go_to_profile_page().pic_l_headshot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_followers_click():
    event_name = "text_followers_click"
    content_type = "user"
    go_to_profile_page().text_followers_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_following_click():
    event_name = "text_following_click"
    content_type = "user"
    go_to_profile_page().text_following_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_joined_click():
    event_name = "text_joined_click"
    content_type = "user"
    go_to_profile_page().text_joined_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_profile_name_click():
    event_name = "text_profile_name_click"
    content_type = "user"
    go_to_profile_page().text_profile_name_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_bio_click_and_text_bio_show():
    event_name = "text_bio_show"
    event_name1 = "text_bio_click"
    content_type = "user"
    go_to_profile_page()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    ProfilePage().text_bio_click()
    result1 = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result1, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_change_page(result1, event_name1, content_type)


def test_btn_editprofile_click():
    event_name = "btn_editprofile_click"
    content_type = "user"
    go_to_profile_page().btn_editprofile_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_btn_share_click():
    event_name = "btn_share_click"
    content_type = "user"
    go_to_profile_page().btn_share_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_btn_contact_click_and_btn_contact_show():
    event_name = "btn_contact_show"
    event_name1 = "btn_contact_click"
    content_type = "user"
    go_to_profile_page().btn_contact_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_change_page(result, event_name1, content_type)


def test_tab_activities_click_and_tab_spots_click():
    event_name = "tab_activities_click"
    content_type = "user"
    go_to_profile_page().tab_activities_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)

    event_name = "tab_spots_click"
    content_type = "user"
    ProfilePage().tab_spots_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_sharespot_show_and_text_sharespot_click():
    event_name = "text_sharespot_show"
    event_name1 = "text_sharespot_click"
    content_type = "user"
    go_to_profile_page().text_sharespot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_change_page(result, event_name1, content_type)


def test_text_url_show_and_text_url_click():
    event_name = "text_url_show"
    event_name1 = "text_url_click"
    content_type = "user"
    go_to_profile_page().text_url_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
    Validators().validate_change_page(result, event_name1, content_type)


def test_icon_more_click():
    event_name = "icon_more_click"
    content_type = "community_comment"
    go_to_profile_page().tab_activities_click()
    ProfilePage().icon_more_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_share_click():
    event_name = "icon_share_click"
    content_type = "community_comment"
    go_to_profile_page().tab_activities_click()
    ProfilePage().icon_share_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_like_click_icon_unlike_click():
    event_name = "icon_like_click"
    event_name2 = "icon_unlike_click"
    content_type = "community_comment"

    go_to_profile_page().tab_activities_click()
    ProfilePage().icon_like_click()

    result1 = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result1, 5)

    ProfilePage().icon_unlike_click()

    result2 = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result2, 5)

    Validators().validate_first_event_name(result1, event_name, content_type)
    Validators().validate_first_event_name(result2, event_name2, content_type)


def test_icon_save_click_icon_unsave_click():
    event_name = "icon_save_click"
    event_name2 = "icon_unsave_click"
    content_type = "community_comment"

    go_to_profile_page().tab_activities_click()
    ProfilePage().icon_save_click()

    result1 = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result1, 5)

    ProfilePage().icon_unsave_click()

    result2 = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result2, 5)

    Validators().validate_first_event_name(result1, event_name, content_type)
    Validators().validate_first_event_name(result2, event_name2, content_type)


def test_icon_comment_click():
    event_name = "icon_comment_click"
    content_type = "community_comment"
    go_to_profile_page().tab_activities_click()
    ProfilePage().icon_comment_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_comment_text_click():
    event_name = "comment_text_click"
    content_type = "community_comment"
    go_to_profile_page().tab_activities_click()
    ProfilePage().comment_text_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_comment_appear():
    event_name = "comment_appear"
    go_to_profile_page().tab_activities_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 10)


def test_comment_disappear():
    event_name = "comment_disappear"
    go_to_profile_page().tab_activities_click()
    ProfilePage().screen_swipeupanddown()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 10)


def test_pic_headshot_click():
    event_name = "pic_headshot_click"
    content_type = "community_comment"
    go_to_profile_page().tab_activities_click()
    ProfilePage().pic_headshot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_username_click():
    event_name = "pic_headshot_click"
    content_type = "community_comment"
    go_to_profile_page().tab_activities_click()
    ProfilePage().text_username_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_card_addprofilepicture_click():
    event_name = "card_addprofilepicture_click"
    content_type = "user"
    go_to_profile_page().card_addprofilepicture_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_card_verifyyouremail_click():
    event_name = "card_verifyyouremail_click"
    content_type = "user"
    go_to_profile_page().card_verifyyouremail_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_communityname_click():
    event_name = "text_communityname_click"
    content_type = "community_comment"
    go_to_profile_page().tab_activities_click()
    ProfilePage().text_communityname_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_icon_back_click():
    event_name = "icon_back_click"
    content_type = "user"
    ADBClient.start_playsee_app().pic_headshot_click().icon_back_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_other_profile_icon_more_click():
    event_name = "icon_more_click"
    content_type = "user"
    ADBClient.start_playsee_app().pic_headshot_click().icon_more_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_btn_follow_click():
    event_name = "btn_follow_click"
    content_type = "user"
    ADBClient.start_playsee_app().pic_headshot_click().btn_follow_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_btn_message_click():
    event_name = "btn_message_click"
    content_type = "user"
    ADBClient.start_playsee_app().pic_headshot_click().btn_message_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_translation_click():
    event_name = "text_translation_click"
    content_type = "user"
    ADBClient.start_playsee_app().pic_headshot_click().text_translation_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)


def test_pic_spot_click():
    event_name = "pic_spot_click"
    content_type = "spot"
    ADBClient.start_playsee_app().pic_headshot_click().tab_spots_click()
    ProfilePage().pic_spot_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)


def test_text_location_show_and_text_location_click():
    event_name1 = "text_location_show"
    event_name = "text_location_click"
    content_type = "community_comment"
    go_to_profile_page().tab_activities_click()
    ProfilePage().text_location_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name1, content_type)
    Validators().validate_change_page(result, event_name, content_type)


def test_comment_media_show_and_comment_media_click():
    event_name1 = "comment_media_show"
    event_name = "comment_media_click"
    content_type = "community_comment"
    go_to_profile_page().tab_activities_click()
    ProfilePage().comment_media_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name1, content_type)
    Validators().validate_change_page(result, event_name, content_type)


def test_text_no_spot_show():
    event_name = "text_no_spot_show"
    content_type = "user"
    ADBClient.start_playsee_app().explore_click().type_tracker_test()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_content_type_in_count(result, event_name, content_type)
