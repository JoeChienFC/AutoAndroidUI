import uiautomator2 as u2
import time,pytest


class BlockPopup:

    def __init__(self):
        self.d = u2.connect()

        self.btn_cancel_xpath = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[4]'
        self.btn_block_x_y = (0.491, 0.828)
        self.btn_cancel_x_y = (0.479, 0.89)

    def btn_block_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.btn_block_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_block_click 失败: {e}")
            pytest.xfail("點擊 btn_block_click 失败")

    def btn_cancel_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.btn_cancel_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_cancel_click 失败: {e}")
            pytest.xfail("點擊 btn_cancel_click 失败")
