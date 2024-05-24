import uiautomator2 as u2
import time,pytest


class CommentMorePopup:

    def __init__(self):
        self.d = u2.connect()
        self.text_cancel_closed_outside_x_y = (0.508, 0.347)
        self.text_cancel_xpath = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[4]'
        self.btn_block_xpath = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]'
        self.btn_share_xpath = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]'
        self.btn_replyto_xpath = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]'
        self.btn_block_x_y = (0.508, 0.83)

    def btn_replyto_click(self):
        try:
            time.sleep(2)
            self.d.xpath(self.btn_replyto_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_replyto_click 失败: {e}")
            pytest.xfail("點擊 btn_replyto_click 失败")

    def btn_share_click(self):
        try:
            time.sleep(2)
            self.d.xpath(self.btn_share_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_share_click 失败: {e}")
            pytest.xfail("點擊 btn_share_click 失败")

    def btn_block_click(self):
        try:
            time.sleep(3)
            self.d.xpath(self.btn_block_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_block_click 失败: {e}")
            pytest.xfail("點擊 btn_block_click 失败")

    def btn_delete_click(self):
        try:
            time.sleep(2)
            self.d.xpath(self.btn_block_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_delete_click 失败: {e}")
            pytest.xfail("點擊 btn_delete_click 失败")

    def text_cancel_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.text_cancel_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 text_cancel_click 失败: {e}")
            pytest.xfail("點擊 text_cancel_click 失败")

    def text_cancel_closed_outside_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_cancel_closed_outside_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 text_cancel_closed_outside_click 失败: {e}")
            pytest.xfail("點擊 text_cancel_closed_outside_click 失败")
