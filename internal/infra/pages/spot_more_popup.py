import uiautomator2 as u2
import time, pytest


class SpotMorePopup:

    def __init__(self):
        self.btn_delete_x_y = (0.482, 0.839)
        self.btn_edit_x_y = (0.494, 0.699)
        self.text_cancel_x_y = (0.502, 0.891)
        self.text_cancel_xpath = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[5]'
        self.d = u2.connect()
        self.btn_collect_xpath = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]'
        self.btn_uncollect_xpath = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]'
        self.btn_download_xpath = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]'
        self.btn_not_interested_xpath = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]'
        self.btn_report_xpath = '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[4]'

        self.btn_collect_x_y = (0.511, 0.636)
        self.btn_uncollect_x_y = (0.511, 0.636)
        self.btn_download_x_y = (0.5, 0.7)

    def btn_collect_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.btn_collect_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 btn_collect 失败 : {e}")

    def btn_uncollect_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.btn_uncollect_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 btn_uncollect 失败 : {e}")

    def btn_download_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.btn_download_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 btn_download 失败 : {e}")

    def btn_notinterested_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.btn_not_interested_xpath).click()

        except Exception as e:
            pytest.xfail(f"點擊 btn_not_interested 失败 : {e}")

    def btn_report_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.btn_report_xpath).click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點擊 btn_report 失败 : {e}")

    def text_cancel_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_cancel_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點擊 text_cancel_click 失败 : {e}")

    def btn_edit_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.btn_edit_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點擊 btn_edit_click 失败 : {e}")

    def btn_delete_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.btn_delete_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點擊 btn_delete_click 失败 : {e}")