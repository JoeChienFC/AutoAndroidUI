import uiautomator2 as u2
import time,pytest
import os


class JoinedCommunity:

    def __init__(self):
        self.list_community_x_y = (0.491, 0.192)
        self.list_result_location_x_y = (0.375, 0.453)
        self.icon_clear_x_y = (0.91, 0.116)
        self.d = u2.connect()
        self.text_done_x_y = (0.908, 0.077)

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
            # os.system('adb shell input text {}'.format('test'))
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

    def list_community_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_community_x_y)

        except Exception as e:
            print(f"點擊 list_community_click 失败: {e}")
            pytest.xfail("點擊 list_community_click 失败")

    def list_result_community_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_community_x_y)
            time.sleep(0.5)

        except Exception as e:
            print(f"點擊 list_result_community_click 失败: {e}")
            pytest.xfail("點擊 list_result_community_click 失败")

    def text_no_result_show(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').click()
            time.sleep(0.5)
            self.d.shell('input text "aaaaa"')
            time.sleep(0.5)

        except Exception as e:
            print(f"點擊 text_no_result_show 失败: {e}")
            pytest.xfail("點擊 text_no_result_show 失败")

    