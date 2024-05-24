import os

import uiautomator2 as u2
import time,pytest


class CommunityLocationPicker:

    def __init__(self):
        self.d = u2.connect()

        self.bar_search = 'bar_search'
        self.icon_clear = 'icon_clear'
        self.icon_close = 'icon_close'
        self.list_recent = 'list_recent'
        self.icon_remove = 'icon_remove'
        self.list_community = 'list_community'
        self.list_result_community_x_y = (0.367, 0.224)

    def bar_search_click(self):
        try:
            time.sleep(1)
            self.d(description=self.bar_search, index=1).click()

        except Exception as e:
            print(f"點擊 bar_search 失败: {e}")
            pytest.xfail("點擊 bar_search 失败")

    def bar_search_typing(self):
        try:
            time.sleep(1)
            self.bar_search_click()
            time.sleep(0.5)
            # self.d.xpath('//android.widget.EditText').set_text("test")
            # os.system('adb shell input text {}'.format("test"))
            self.d.shell('input text "test"')

        except Exception as e:
            print(f"點擊 bar_search_typing 失败: {e}")
            pytest.xfail("點擊 bar_search_typing 失败")

    def icon_clear_click(self):
        try:
            time.sleep(1)
            self.bar_search_typing()
            time.sleep(0.5)
            self.d(description=self.icon_clear).click()

        except Exception as e:
            print(f"點擊 icon_clear 失败: {e}")
            pytest.xfail("點擊 icon_clear 失败")

    def icon_close_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_close).click()

        except Exception as e:
            print(f"點擊 icon_close 失败: {e}")
            pytest.xfail("點擊 icon_close 失败")

    def list_recent_click(self):
        try:
            time.sleep(1)
            if self.d(description='Recent').exists(3):
                self.d(description=self.list_recent).click()
            else:
                self.list_community_click()
            time.sleep(0.5)

        except Exception as e:
            print(f"點擊 list_recent 失败: {e}")
            pytest.xfail("點擊 list_recent 失败")

    def icon_remove_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_remove).click()
            time.sleep(0.5)

        except Exception as e:
            print(f"點擊 icon_remove 失败: {e}")
            pytest.xfail("點擊 icon_remove 失败")

    def list_community_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_community).click()

        except Exception as e:
            print(f"點擊 list_community 失败: {e}")
            pytest.xfail("點擊 list_community 失败")

    def list_result_community_click(self):
        try:
            time.sleep(1)
            # os.system('adb shell input text {}'.format("test"))
            self.bar_search_typing()
            time.sleep(2)
            self.d.click(*self.list_result_community_x_y)

        except Exception as e:
            print(f"點擊 list_result_community 失败: {e}")
            pytest.xfail("點擊 list_result_community 失败")

    def text_no_result_show(self):
        try:
            time.sleep(1)
            # self.d.xpath('//android.widget.EditText').set_text("lllll")
            # os.system('adb shell input text {}'.format("lllll"))
            self.bar_search_click()
            time.sleep(0.5)
            self.d.shell('input text "lllll"')

        except Exception as e:
            print(f"text_no_result_show 失败: {e}")
            pytest.xfail("text_no_result_show 失败")

