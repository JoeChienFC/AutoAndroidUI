import uiautomator2 as u2
import time, pytest


class SpotMorePopup:

    def __init__(self):
        self.btn_delete_x_y = (0.482, 0.839)
        self.btn_edit_x_y = (0.494, 0.699)

        self.text_cancel = "text_cancel"
        self.d = u2.connect()
        self.btn_download = "btn_download"
        self.btn_not_interested = "btn_not_interested"
        self.btn_report = "btn_report"

    def btn_download_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_download).click()

        except Exception as e:
            pytest.xfail(f"點擊 btn_download 失败 : {e}")

    def btn_notinterested_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_not_interested).click()

        except Exception as e:
            pytest.xfail(f"點擊 btn_not_interested 失败 : {e}")

    def btn_report_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_report).click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點擊 btn_report 失败 : {e}")

    def text_cancel_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_cancel).click()
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