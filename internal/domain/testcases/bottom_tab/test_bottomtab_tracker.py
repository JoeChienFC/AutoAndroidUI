from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.popUp import PopUp


def test_bottom_tab_ai_click():
    event_name = "bottomtab_ai_click"
    ADBClient.start_playsee_app().ai_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    print(f"bigquery : {result[1]}")

    assert result[0]['event_name'] == 'screen_view' or result[1][
        'event_name'] == 'screen_view', "Test failed: event_name is not 'screen_view' in result"
    assert result[1]['event_name'] == event_name, f"Test failed: {event_name} event in bigquery"


def test_bottom_tab_community_click():
    event_name = "bottomtab_community_click"
    ADBClient.start_playsee_app().community_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    for i in range(5):
        print(f"bigquery : {result[i]}")

    assert any(result[i]['event_name'] == event_name for i in range(5)), f"Test failed: {event_name} event in bigquery"


def test_bottom_tab_explore_click():
    event_name = "bottomtab_explore_click"
    ADBClient.start_playsee_app().explore_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    print(f"bigquery : {result[2]}")

    assert result[0]['event_name'] == 'screen_view' or result[1][
        'event_name'] == 'screen_view', "Test failed: event_name is not 'screen_view' in result"
    assert result[2]['event_name'] == event_name, f"Test failed: {event_name} event in bigquery"


def test_bottom_tab_my_profile_click():
    event_name = "bottomtab_myprofile_click"
    ADBClient.start_playsee_app().myprofile_click()
    PopUp().pop_up_13_years_old()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    print(f"bigquery0 : {result[0]}")
    print(f"bigquery1 : {result[1]}")

    assert result[0]['event_name'] == 'screen_view' or result[1][
        'event_name'] == 'screen_view', "Test failed: event_name is not 'screen_view' in result"
    assert result[0]['event_name'] == event_name or result[1][
        'event_name'] == event_name, f"Test failed: event_name is not {event_name} in result"


def test_bottom_tab_spot_click():
    event_name = "bottomtab_spot_click"
    ADBClient.start_playsee_app().spot_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    print(f"bigquery0 : {result[0]}")
    print(f"bigquery1 : {result[1]}")

    assert result[0]['event_name'] == 'screen_view' or result[1][
        'event_name'] == 'screen_view', "Test failed: event_name is not 'screen_view' in result"
    assert result[1]['event_name'] == event_name or result[2][
        'event_name'] == event_name, f"Test failed: event_name is not {event_name} in result"
