import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.validators.validators import Validators


def test_list_notifications_show_and_list_notifications_click():
    event_name = "list_notifications_click"
    event_name1 = "list_notifications_show"
    content_type = "spot"
    ADBClient.start_playsee_app().tab_notifications_click().list_notifications_click()

    result = BigQueryFunction().fetch_user_operation_tracker()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name1, 10)
    Validators().validate_change_page(result, event_name, content_type)

