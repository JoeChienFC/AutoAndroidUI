import uiautomator2 as u2
import time, pytest


class SpotMorePopup:

    def __init__(self):
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

    def btn_not_interested_click(self):
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

