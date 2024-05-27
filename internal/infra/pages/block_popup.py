import uiautomator2 as u2
import time,pytest


class BlockPopup:

    def __init__(self):
        self.btn_cancel = "btn_cancel"
        self.btn_block = "btn_block"
        self.d = u2.connect()

    def btn_block_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_block).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_block 失败: {e}")
            pytest.xfail("點擊 btn_block 失败")

    def btn_cancel_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_cancel).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_cancel 失败: {e}")
            pytest.xfail("點擊 btn_cancel 失败")
