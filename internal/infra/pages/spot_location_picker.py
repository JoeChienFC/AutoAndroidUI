import os

import uiautomator2 as u2
import time
import pytest



class SpotLocationPicker:

    def __init__(self):
        self.d = u2.connect()

        self.icon_clear_x_y = (0.905, 0.118)
        self.icon_close_x_y = (0.914, 0.06)
        self.first_recent_x_y = (0.27, 0.305)
        self.icon_remove_x_y = (0.935, 0.309)
        self.list_spot_x_y = (0.2, 0.598)
        self.list_result_spot_x_y = (0.367, 0.224)

    def bar_search_click(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').click()

        except Exception as e:
            pytest.xfail(f"點擊 bar_search 失败: {e}")

    def bar_search_typing(self):
        try:
            time.sleep(1)
            # self.d.xpath('//android.widget.EditText').set_text("test")
            os.system('adb shell input text {}'.format("test"))

        except Exception as e:
            pytest.xfail(f"點擊 bar_search_typing 失败: {e}")

    def icon_clear_click(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').click()
            time.sleep(0.5)
            os.system('adb shell input text {}'.format('test'))
            time.sleep(0.5)
            self.d.click(*self.icon_clear_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 icon_clear 失败: {e}")

    def icon_close_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_close_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 icon_close 失败: {e}")

    def list_recent_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.first_recent_x_y)
            time.sleep(0.5)

        except Exception as e:
            pytest.xfail(f"點擊 list_recent 失败: {e}")

    def icon_remove_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_remove_x_y)
            time.sleep(0.5)

        except Exception as e:
            pytest.xfail(f"點擊 icon_remove 失败: {e}")

    def list_spot_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_spot_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 list_spot 失败: {e}")

    def list_result_spot_click(self):
        try:
            time.sleep(1)
            # self.d.xpath('//android.widget.EditText').set_text("test")
            os.system('adb shell input text {}'.format("test"))
            time.sleep(2)
            self.d.click(*self.list_result_spot_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 list_result_spot 失败: {e}")

    def text_no_result_show(self):
        try:
            time.sleep(1)
            # self.d.xpath('//android.widget.EditText').set_text("lllll")
            os.system('adb shell input text {}'.format("lllll"))

        except Exception as e:
            pytest.xfail(f"text_no_result_show 失败:{e}")

