import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.new_account_profile_page import NewAccountProfilePage
from internal.infra.validators.validators import Validators


def go_to_profile_page():
    ADBClient.start_playsee_app().myprofile_click()

    return NewAccountProfilePage()


def test_card_addbio_click():
    event_name = "card_addbio_click"
    content_type = "user"
    go_to_profile_page().card_addbio_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)

