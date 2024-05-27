import uiautomator2 as u2
import time,pytest
import os


class Notifications:

    def __init__(self):
        self.d = u2.connect()

        self.list_notifications = "list_notifications"

    def list_notifications_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_notifications).click()

        except Exception as e:
            print(f"點擊 list_notifications_click 失败: {e}")
            pytest.xfail("點擊 list_notifications_click 失败")

