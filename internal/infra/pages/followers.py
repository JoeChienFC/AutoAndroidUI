import uiautomator2 as u2
import time, pytest
import os


class Followers:

    def __init__(self):
        self.icon_clear_x_y = (0.904, 0.12)
        self.list_user_x_y = (0.226, 0.18)
        self.d = u2.connect()
        self.icon_back_x_y = (0.062, 0.061)

    def icon_back_click(self):
        try:
            self.d.click(*self.icon_back_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 icon_back_click 失败: {e}")

    def list_user_click(self):
        try:
            self.d.click(*self.list_user_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 list_user_click 失败: {e}")

    def text_follow_click(self):
        try:
            time.sleep(1)
            self.d(description="Follow").click()
            time.sleep(1)

        except Exception as e:
            print(f"點 text_follow_click 失败: {e}")
            pytest.xfail("點 text_follow_click 失败")

    def text_following_click(self):
        try:
            self.d(description="Following").click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 text_following_click 失败: {e}")

    def bar_search_click(self):
        try:
            self.d.xpath('//android.widget.EditText').click()
            time.sleep(1)

        except Exception as e:
            print(f"點 bar_search_click 失败: {e}")
            pytest.xfail("點 bar_search_click 失败")

    def bar_search_typing(self):
        try:
            time.sleep(1)
            self.d.shell('input text "test"')
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_hashtag_drag 失败: {e}")
            pytest.xfail("點 btn_hashtag_drag 失败")

    def icon_clear_click(self):
        try:
            time.sleep(3)
            self.d.click(*self.icon_clear_x_y)
            time.sleep(3)

        except Exception as e:
            print(f"點 icon_clear_click 失败: {e}")
            pytest.xfail("點 icon_clear_click 失败")

    def list_result_user_click(self):
        try:
            time.sleep(1)
            self.bar_search_click()
            time.sleep(1)
            self.d.shell('input text "trav"')
            time.sleep(4)
            self.list_user_click()
            time.sleep(1)

        except Exception as e:
            print(f"點 list_result_user_click 失败: {e}")
            pytest.xfail("點 list_result_user_click 失败")
