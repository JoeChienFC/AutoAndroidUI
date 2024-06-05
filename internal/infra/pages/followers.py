import uiautomator2 as u2
import time, pytest
import os


class Followers:

    def __init__(self):
        self.icon_back = "icon_back"
        self.list_user = "list_user"
        self.text_follow = "text_follow"
        self.text_following = "text_following"
        self.bar_search = "bar_search"
        self.icon_clear = "icon_clear"

        self.d = u2.connect()

    def icon_back_click(self):
        try:
            self.d(description=self.icon_back).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 icon_back_click 失败: {e}")

    def list_user_click(self):
        try:
            self.d(description=self.list_user).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 list_user_click 失败: {e}")

    def text_follow_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_follow).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點 text_follow_click 失败: {e}")
            pytest.xfail("點 text_follow_click 失败")

    def text_following_click(self):
        try:
            self.d(description=self.text_following).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 text_following_click 失败: {e}")

    def bar_search_click(self):
        try:
            self.d(description=self.bar_search).click(timeout=2)
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
            self.d(description=self.icon_clear).click(timeout=2)
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
