import uiautomator2 as u2
import time, pytest


class DmMessagePopup:

    def __init__(self):
        self.d = u2.connect()

    def btn_unsend_click(self):
        try:
            time.sleep(1)
            self.d(className="android.view.View", index=1).click()

        except Exception as e:
            pytest.xfail(f"點擊 btn_uncollect 失败 : {e}")

    def btn_copy_click(self):
        try:
            time.sleep(1)
            self.d(className="android.view.View", index=0).click()

        except Exception as e:
            pytest.xfail(f"點擊 btn_download 失败 : {e}")

    def text_cancel_click(self):
        try:
            time.sleep(1)
            self.d(className="android.view.View", index=2).click()

        except Exception as e:
            pytest.xfail(f"點擊 text_cancel_click 失败 : {e}")
