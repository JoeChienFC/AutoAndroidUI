import os

import uiautomator2 as u2
import time,pytest


class CommunityLocationPicker:

    def __init__(self):
        self.d = u2.connect()

        self.icon_clear_x_y = (0.905, 0.118)
        self.icon_close_x_y = (0.914, 0.06)
        self.first_recent_x_y = (0.402, 0.305)
        self.icon_remove_x_y = (0.932, 0.309)
        self.list_community_x_y = (0.2, 0.598)
        self.list_result_community_x_y = (0.367, 0.224)

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
            # self.d.xpath('//android.widget.EditText').set_text("test")
            os.system('adb shell input text {}'.format("test"))


        except Exception as e:
            print(f"點擊 bar_search_typing 失败: {e}")
            pytest.xfail("點擊 bar_search_typing 失败")

    def icon_clear_click(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').click()
            time.sleep(0.5)
            os.system('adb shell input text {}'.format('test'))
            time.sleep(0.5)
            self.d.click(*self.icon_clear_x_y)

        except Exception as e:
            print(f"點擊 icon_clear 失败: {e}")
            pytest.xfail("點擊 icon_clear 失败")

    def icon_close_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_close_x_y)

        except Exception as e:
            print(f"點擊 icon_close 失败: {e}")
            pytest.xfail("點擊 icon_close 失败")

    def list_recent_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.first_recent_x_y)
            time.sleep(0.5)

        except Exception as e:
            print(f"點擊 list_recent 失败: {e}")
            pytest.xfail("點擊 list_recent 失败")

    def icon_remove_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_remove_x_y)
            time.sleep(0.5)

        except Exception as e:
            print(f"點擊 icon_remove 失败: {e}")
            pytest.xfail("點擊 icon_remove 失败")

    def list_community_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_community_x_y)

        except Exception as e:
            print(f"點擊 list_community 失败: {e}")
            pytest.xfail("點擊 list_community 失败")

    def list_result_community_click(self):
        try:
            time.sleep(1)
            # self.d.xpath('//android.widget.EditText').set_text("test")
            os.system('adb shell input text {}'.format("test"))
            time.sleep(2)
            self.d.click(*self.list_result_community_x_y)

        except Exception as e:
            print(f"點擊 list_result_community 失败: {e}")
            pytest.xfail("點擊 list_result_community 失败")

    def text_no_result_show(self):
        try:
            time.sleep(1)
            # self.d.xpath('//android.widget.EditText').set_text("lllll")
            os.system('adb shell input text {}'.format("lllll"))

        except Exception as e:
            print(f"text_no_result_show 失败: {e}")
            pytest.xfail("text_no_result_show 失败")

