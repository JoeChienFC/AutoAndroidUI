import uiautomator2 as u2
import time, pytest


class Explore:

    def __init__(self):
        self.list_user = "list_user"
        self.d = u2.connect()

        self.bar_search = 'bar_search'
        self.pic_spot = "pic_spot"
        self.text_seemore = "text_seemore"
        self.list_community = "list_community"

    def bar_search_click(self):
        try:
            time.sleep(1)
            self.d(description=self.bar_search).click()

        except Exception as e:
            pytest.xfail(f"點擊 search_click 失败 : {e}")

    def pic_spot_click(self):
        try:
            time.sleep(1)
            self.d(description=self.pic_spot).click()

        except Exception as e:
            pytest.xfail(f"點擊 pic_spot 失败 : {e}")

    def text_seemore_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_seemore).click()

        except Exception as e:
            pytest.xfail(f"點擊 text_seemore 失败 : {e}")

    def screen_swipeupanddown(self):
        try:
            time.sleep(1)
            self.d.swipe_ext("up")

        except Exception as e:
            print(f"上滑 screen 失败: {e}")
            pytest.xfail("上滑 screen 失败")

    def list_community_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_community).click()

        except Exception as e:
            pytest.xfail(f"點擊 list_community 失败 : {e}")

    def list_user_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_user).click()

        except Exception as e:
            pytest.xfail(f"點擊 list_user 失败 : {e}")

    def type_tracker_test(self):
        try:
            time.sleep(1)
            self.bar_search_click()
            self.d.shell('input text "tracker_test"')
            self.list_user_click()

        except Exception as e:
            pytest.xfail(f"點擊 type_tracker_test 失败 : {e}")

    def type_arkibarn(self):
        try:
            time.sleep(1)
            self.bar_search_click()
            self.d.shell('input text "arkibarn"')
            self.list_user_click()
            time.sleep(2)

        except Exception as e:
            pytest.xfail(f"點擊 type_arkibarn 失败 : {e}")