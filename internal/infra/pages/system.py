import uiautomator2 as u2
import time, pytest


class System:

    def __init__(self):
        self.d = u2.connect()

    def back_click(self):
        try:
            self.d.press("back")
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 system back 失敗: {e}")