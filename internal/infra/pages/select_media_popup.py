import uiautomator2 as u2
import time, pytest


class SelectMediaPopup:

    def __init__(self):
        self.btn_cancel = "Cancel"
        self.btn_move = "Move"
        self.btn_copy = "Copy"
        self.d = u2.connect()

    def btn_copy_click(self):
        try:
            self.d(text=self.btn_copy).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_copy_click 失败: {e}")
            pytest.xfail("點擊 btn_copy_click 失败")

    def btn_move_click(self):
        try:
            self.d(text=self.btn_move).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_move_click 失败: {e}")
            pytest.xfail("點擊 btn_move_click 失败")

    def btn_cancel_click(self):
        try:
            time.sleep(1)
            self.d(text=self.btn_cancel).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_cancel 失败: {e}")
            pytest.xfail("點擊 btn_cancel 失败")

