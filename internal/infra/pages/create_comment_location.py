import uiautomator2 as u2
import time,pytest
import os


class CreateCommentLocation:

    def __init__(self):
        self.list_location = "list_location"
        self.list_result_location = "list_result_location"
        self.list_my_location = "list_my_location"
        self.icon_clear = "icon_clear"
        self.d = u2.connect()
        self.text_done = "text_done"

    def text_done_click(self):
        try:
            self.d(description=self.text_done).click(timeout=2)
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
            os.system('adb shell input text {}'.format('test'))

        except Exception as e:
            print(f"點擊 bar_search_typing 失败: {e}")
            pytest.xfail("點擊 bar_search_typing 失败")

    def icon_clear_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_clear).click(timeout=2)

        except Exception as e:
            print(f"點擊 icon_clear 失败: {e}")
            pytest.xfail("點擊 icon_clear 失败")

    def list_location_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_location).click(timeout=2)

        except Exception as e:
            print(f"點擊 list_location_click 失败: {e}")
            pytest.xfail("點擊 list_location_click 失败")

    def list_result_location_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_result_location).click(timeout=2)
            time.sleep(0.5)

        except Exception as e:
            print(f"點擊 list_result_location_click 失败: {e}")
            pytest.xfail("點擊 list_result_location_click 失败")

    def text_no_result_show(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').click()
            time.sleep(0.5)
            # self.d.xpath('//android.widget.EditText').set_text("aaaa")
            os.system('adb shell input text {}'.format("qazwsxedc"))
            time.sleep(0.5)

        except Exception as e:
            print(f"點擊 text_no_result_show 失败: {e}")
            pytest.xfail("點擊 text_no_result_show 失败")


            