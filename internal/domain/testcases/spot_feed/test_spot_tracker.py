import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.homefeed import HomeFeed


def test_btn_location_picker_click():
    event_name = "btn_locationpicker_click"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click().location_picker_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    print(f"bigquery : {result[0]}")

    assert result[0]['event_name'] == 'screen_view' or result[1][
        'event_name'] == 'screen_view', "Test failed: event_name is not 'screen_view' in result"
    assert result[0]['event_name'] == event_name or result[1][
        'event_name'] == event_name, f"Test failed: {event_name} event in bigquery"

    assert any('parameters' in result[i] and result[i]['parameters'].get('content_type') == content_type for i in
               range(2)), f"Test failed: {content_type} event in bigquery"


def test_icon_create_click():
    event_name = "icon_create_click"
    content_type = "spot"
    ADBClient.start_playsee_app().spot_click().icon_create_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    # 會觸發其他 tracker
    print(f"bigquery : {result[2]}")

    assert result[0]['event_name'] == 'screen_view' or result[1][
        'event_name'] == 'screen_view', "Test failed: event_name is not 'screen_view' in result"
    assert result[2]['event_name'] == event_name, f"Test failed: {event_name} event in bigquery"
    assert result[2]['parameters'].get('content_type') == content_type, f"Test failed: {content_type} event in bigquery"


def test_btn_follow_click():
    event_name = "btn_follow_click"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().btn_follow_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    print(f"bigquery : {result[0]}")

    HomeFeed().btn_unfollow_click()

    assert result[0]['event_name'] == event_name, f"Test failed: {event_name} event in bigquery"
    assert result[0]['parameters']["content_type"] == content_type, f"Test failed: {content_type} event in bigquery"


def test_icon_like_click():
    event_name = "icon_like_click"
    content_type = "spot"

    ADBClient.start_playsee_app().spot_click().btn_follow_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    print(f"bigquery : {result[0]}")

    HomeFeed().btn_unfollow_click()

    assert result[0]['event_name'] == event_name, f"Test failed: {event_name} event in bigquery"
    assert result[0]['parameters']["content_type"] == content_type, f"Test failed: {content_type} event in bigquery"
