from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.popUp import PopUp


def test_bottom_tab_ai_click():
    event_name = "bottomtab_ai_click"
    ADBClient.start_playsee_app().ai_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    assert result[0]['event_name'] == 'screen_view' or result[1][
        'event_name'] == 'screen_view', "Test failed: event_name is not 'screen_view' in result"
    assert result[1]['event_name'] == event_name or result[2][
        'event_name'] == event_name, f"Test failed: event_name is not {event_name} in result"


def test_bottom_tab_community_click():
    event_name = "bottomtab_community_click"
    ADBClient.start_playsee_app().community_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 10)

    assert any(item['event_name'] == event_name for item in
               result[:10]), f"Test failed: event_name is not {event_name} in result"


def test_bottom_tab_explore_click():
    event_name = "bottomtab_explore_click"
    ADBClient.start_playsee_app().explore_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    assert result[0]['event_name'] == 'screen_view' or result[1][
        'event_name'] == 'screen_view', "Test failed: event_name is not 'screen_view' in result"
    assert result[1]['event_name'] == event_name or result[2][
        'event_name'] == event_name, f"Test failed: event_name is not {event_name} in result"


def test_bottom_tab_my_profile_click():
    event_name = "bottomtab_myprofile_click"
    ADBClient.start_playsee_app().myprofile_click()
    PopUp().pop_up_13_years_old()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    assert result[0]['event_name'] == 'screen_view' or result[1][
        'event_name'] == 'screen_view', "Test failed: event_name is not 'screen_view' in result"
    assert result[1]['event_name'] == event_name or result[2][
        'event_name'] == event_name, f"Test failed: event_name is not {event_name} in result"


def test_bottom_tab_spot_click():
    event_name = "bottomtab_spot_click"
    ADBClient.start_playsee_app().spot_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    assert any(
        item['event_name'] == 'screen_view' for item in result[:10]), "Test failed: 'screen_view' not found in result"
    index_of_screen_view = next((i for i, item in enumerate(result[:10]) if item['event_name'] == 'screen_view'), None)
    assert index_of_screen_view is not None, "Test failed: 'screen_view' not found in result"
    assert any(item['event_name'] == event_name for item in
               result[:index_of_screen_view]), f"Test failed: event_name is not {event_name} in result"

