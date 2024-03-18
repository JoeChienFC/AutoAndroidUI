import time

from google.cloud import bigquery
from datetime import datetime, timedelta


class BigQueryFunction:
    def __init__(self):
        pass

    def fetch_user_operation_tracker(self):
        time.sleep(1)
        project_id = "framy-stage"
        user_id = "1794709464127508481"
        # 設定 BigQuery 客戶端
        client = bigquery.Client(project=project_id)

        # 取得今天的日期
        today = datetime.now().strftime("%Y-%m-%d")

        # 構建 SQL 查詢
        query = f"""
            SELECT event_name, event_timestamp, parameters
            FROM `framy-stage.bi_raws.log_events`
            WHERE user_id = '{user_id}'
              AND TIMESTAMP_TRUNC(event_timestamp, DAY) = TIMESTAMP("{today}")
            ORDER BY event_timestamp DESC
            LIMIT 10
        """

        query_job = client.query(query)
        results = query_job.result()

        # 創建一個結構化的數據列表
        structured_data = []

        for row in results:
            # 提取欄位值
            event_name = row[0]
            event_timestamp = row[1]
            parameters = row[2]

            # 將提取的值組合成一個結構化的數據字典
            data_entry = {
                'event_name': event_name,
                'event_timestamp': event_timestamp,
                'parameters': parameters,
            }

            # 將結構化的數據字典添加到列表中
            structured_data.append(data_entry)

        # 返回結構化的數據列表
        return structured_data

    def display_query_result(self, result, times):
        print("------ 以下為 tracker 結果越上面時間越新 -----------")
        for i in range(times):
            print(f"bigquery : {result[i]}")

        print("------------------------------------------------")

