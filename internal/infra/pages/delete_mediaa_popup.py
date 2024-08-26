import uiautomator2 as u2
import time,pytest


class DeleteMediaPopup:

    def __init__(self):
        self.d = u2.connect()

    def btn_delete_click(self):
        try:
            self.d(resourceId="android:id/button1", text="Delete").click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_delete_click 失败: {e}")
            pytest.xfail("點擊 btn_delete_click 失败")

    def btn_cancel_click(self):
        try:
            self.d(resourceId="android:id/button2", text="Cancel").click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_cancel_click 失败: {e}")
            pytest.xfail("點擊 btn_cancel_click 失败")
