from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.popUp import PopUp
from internal.infra.validators.validators import Validators


def test_bottom_tab_ai_click():
    event_name = "bottomtab_ai_click"
    ADBClient.start_playsee_app().ai_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_bottom_tab_community_click():
    event_name = "bottomtab_community_click"
    ADBClient.start_playsee_app().community_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 10)

    Validators().validate_event_name_in_count(result, event_name, 10)


def test_bottom_tab_explore_click():
    event_name = "bottomtab_explore_click"
    ADBClient.start_playsee_app().explore_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_bottom_tab_my_profile_click():
    event_name = "bottomtab_myprofile_click"
    ADBClient.start_playsee_app().myprofile_click()
    PopUp().pop_up_13_years_old()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_bottom_tab_spot_click():
    event_name = "bottomtab_spot_click"
    ADBClient.start_playsee_app().spot_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)

