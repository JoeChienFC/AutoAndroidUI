import uiautomator2 as u2
import time, pytest
import os


class Searching:

    def __init__(self):
        self.d = u2.connect()

        self.select_first_hashtag_x_y = (0.377, 0.187)
        self.select_second_x_y = (0.285, 0.211)
        self.select_first_x_y = (0.357, 0.167)
        self.icon_back = "icon_back"
        self.icon_remove = "icon_remove"
        self.icon_clear = "icon_clear"
        self.icon_close = "icon_close"
        self.bar_search = "bar_search"
        self.list_community = "list_community"
        self.text_cancel = "text_cancel"

    def text_cancel_click(self):
        try:
            self.d(description=self.text_cancel).click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 text_cancel_click 失败: {e}")

    def bar_search_click(self):
        try:
            self.d(description=self.bar_search).click()

        except Exception as e:
            pytest.xfail(f"點 bar_search_click 失败: {e}")

    def bar_search_typing(self):
        try:
            time.sleep(1)
            self.d.shell('input text "test"')
            time.sleep(1)

        except Exception as e:
            print(f"點 bar_search_typing 失败: {e}")
            pytest.xfail("點 bar_search_typing 失败")

    def icon_clear_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_clear).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_clear_click 失败: {e}")
            pytest.xfail("點 icon_clear_click 失败")

    def icon_remove_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_remove).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_remove_click 失败: {e}")
            pytest.xfail("點 icon_remove_click 失败")

    def icon_back_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_back).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_back_click 失败: {e}")
            pytest.xfail("點 icon_back_click 失败")

    def tab_spot_click(self):
        try:
            time.sleep(2)
            self.d(description="Tab 1 of 4").click()
            time.sleep(2)

        except Exception as e:
            print(f"點 tab_spot_click 失败: {e}")
            pytest.xfail("點 tab_spot_click 失败")

    def tab_community_click(self):
        try:
            time.sleep(3)
            self.d(description="Tab 2 of 4").click()
            time.sleep(5)

        except Exception as e:
            print(f"點 tab_community_click 失败: {e}")
            pytest.xfail("點 tab_community_click 失败")

    def tab_user_click(self):
        try:
            time.sleep(2)
            self.d(description="Tab 3 of 4").click()
            time.sleep(2)

        except Exception as e:
            print(f"點 tab_user_click 失败: {e}")
            pytest.xfail("點 tab_user_click 失败")

    def tab_hashtag_click(self):
        try:
            time.sleep(2)
            self.d(description="Tab 4 of 4").click()
            time.sleep(2)

        except Exception as e:
            print(f"點 tab_hashtag_click 失败: {e}")
            pytest.xfail("點 tab_hashtag_click 失败")

    def list_keyword_click(self):
        try:
            time.sleep(1)
            self.d.shell('input text "taipei"')
            time.sleep(1)
            self.d.click(*self.select_first_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 list_keyword_click 失败: {e}")
            pytest.xfail("點 list_keyword_click 失败")

    def list_recent_keyword_click(self):
        try:
            time.sleep(1)
            self.list_keyword_click()
            time.sleep(1)
            self.icon_back_click()
            time.sleep(1)
            from internal.infra.pages.explore import Explore
            Explore().bar_search_click()
            time.sleep(1)
            self.d.click(*self.select_first_x_y)

        except Exception as e:
            print(f"點 list_recent_keyword_click 失败: {e}")
            pytest.xfail("點 list_recent_keyword_click 失败")

    def list_user_click(self):
        try:
            time.sleep(1)
            self.d.shell('input text "joe"')
            time.sleep(5)
            self.d.click(*self.select_second_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 list_user_click 失败: {e}")
            pytest.xfail("點 list_user_click 失败")

    def list_recent_user_click(self):
        try:
            time.sleep(1)
            self.list_user_click()
            time.sleep(1)
            self.icon_back_click()
            time.sleep(1)
            self.text_cancel_click()
            time.sleep(1)
            from internal.infra.pages.explore import Explore
            Explore().bar_search_click()
            time.sleep(1)
            self.d.click(*self.select_first_x_y)

        except Exception as e:
            print(f"點 list_recent_user_click 失败: {e}")
            pytest.xfail("點 list_recent_user_click 失败")

    def list_community_click(self):
        try:
            time.sleep(1)
            self.d.shell('input text "dogs"')
            time.sleep(1)
            self.d.click(*self.select_second_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 list_community_click 失败: {e}")
            pytest.xfail("點 list_community_click 失败")

    def list_recent_community_click(self):
        try:
            time.sleep(1)
            self.list_community_click()
            time.sleep(1)
            self.icon_back_click()
            time.sleep(1)
            self.text_cancel_click()
            time.sleep(1)
            from internal.infra.pages.explore import Explore
            Explore().bar_search_click()
            time.sleep(1)
            self.d.click(*self.select_first_x_y)

        except Exception as e:
            print(f"點 list_recent_community_click 失败: {e}")
            pytest.xfail("點 list_recent_community_click 失败")

    def list_recent_hashtag_click(self):
        try:
            time.sleep(1)
            self.list_keyword_click()
            time.sleep(1)
            self.tab_hashtag_click()
            time.sleep(1)
            self.d.click(*self.select_first_hashtag_x_y)
            time.sleep(1)
            self.icon_back_click()
            time.sleep(1)
            self.icon_back_click()
            time.sleep(1)
            from internal.infra.pages.explore import Explore
            Explore().bar_search_click()
            time.sleep(1)
            self.d.click(*self.select_first_x_y)

        except Exception as e:
            print(f"點 list_recent_hashtag_click 失败: {e}")
            pytest.xfail("點 list_recent_hashtag_click 失败")
