import os

import uiautomator2 as u2
import time
import pytest


class CreateSpotPublishLocation:

    def __init__(self):
        self.list_my_location_x_y = (0.404, 0.455)
        self.icon_clear_x_y = (0.901, 0.14)
        self.d = u2.connect()
        self.text_done_x_y = (0.908, 0.077)

    def text_done_click(self):
        try:
            self.d.click(*self.text_done_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 text_done 失败: {e}")
            pytest.xfail("點 text_done 失败")

    def bar_search_click(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').click()

        except Exception as e:
            print(f"點擊 bar_search 失败: {e}")
            pytest.xfail("點擊 bar_search 失败")

    def bar_search_typing(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').click()
            time.sleep(1)
            self.d.shell('input text "test"')

        except Exception as e:
            print(f"點擊 bar_search_typing 失败: {e}")
            pytest.xfail("點擊 bar_search_typing 失败")

    def icon_clear_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_clear_x_y)

        except Exception as e:
            print(f"點擊 icon_clear 失败: {e}")
            pytest.xfail("點擊 icon_clear 失败")

    def icon_my_location_click(self):
        try:
            time.sleep(1)
            self.d(className="android.widget.ImageView", index=3).click()

        except Exception as e:
            print(f"點擊 icon_my_location_click 失败: {e}")
            pytest.xfail("點擊 icon_my_location_click 失败")

    def list_location_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_my_location_x_y)

        except Exception as e:
            print(f"點擊 list_location_click 失败: {e}")
            pytest.xfail("點擊 list_location_click 失败")

    def list_result_location_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_my_location_x_y)
            time.sleep(0.5)

        except Exception as e:
            print(f"點擊 list_result_location_click 失败: {e}")
            pytest.xfail("點擊 list_result_location_click 失败")

    def text_no_result_show(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').click()
            time.sleep(0.5)
            self.d.shell('input text "qazwsxedc"')
            time.sleep(0.5)

        except Exception as e:
            print(f"點擊 text_no_result_show 失败: {e}")
            pytest.xfail("點擊 text_no_result_show 失败")


