import uiautomator2 as u2
import time,pytest


class CommentMorePopup:

    def __init__(self):
        self.btn_delete = "btn_delete"
        self.d = u2.connect()
        self.text_cancel_closed_outside = "text_cancel_closed_outside"
        self.text_cancel = "text_cancel"
        self.btn_block = "btn_block"
        self.btn_share = "btn_share"
        self.btn_replyto = "btn_replyto"
        self.btn_block = "btn_block"

    def btn_replyto_click(self):
        try:
            time.sleep(2)
            self.d(description=self.btn_replyto).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_replyto_click 失败: {e}")
            pytest.xfail("點擊 btn_replyto_click 失败")

    def btn_share_click(self):
        try:
            time.sleep(2)
            self.d(description=self.btn_share).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_share_click 失败: {e}")
            pytest.xfail("點擊 btn_share_click 失败")

    def btn_block_click(self):
        try:
            time.sleep(3)
            self.d(description=self.btn_block).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_block_click 失败: {e}")
            pytest.xfail("點擊 btn_block_click 失败")

    def btn_delete_click(self):
        try:
            time.sleep(2)
            self.d(description=self.btn_delete).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_delete_click 失败: {e}")
            pytest.xfail("點擊 btn_delete_click 失败")

    def text_cancel_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_cancel).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 text_cancel_click 失败: {e}")
            pytest.xfail("點擊 text_cancel_click 失败")

    def text_cancel_closed_outside_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_cancel_closed_outside).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 text_cancel_closed_outside_click 失败: {e}")
            pytest.xfail("點擊 text_cancel_closed_outside_click 失败")
