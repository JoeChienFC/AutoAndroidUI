import uiautomator2 as u2
import time,pytest


class ShareToPopup:

    def __init__(self):
        self.d = u2.connect()
        self.first_community_x_y = (0.479, 0.448)

    def list_community_click(self):
        try:
            time.sleep(3)
            self.d.click(*self.first_community_x_y)

        except Exception as e:
            print(f"選第一個 community 失败: {e}")
            pytest.xfail("選第一個 community 失败")

    def bar_comment_click(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText[2]').click()

        except Exception as e:
            print(f"bar_comment_click 失败: {e}")
            pytest.xfail("bar_comment_click 失败")

    def bar_comment_typing(self):
        try:
            time.sleep(1)
            self.d.shell('input text "test"')

        except Exception as e:
            print(f"bar_comment_typing 失败: {e}")
            pytest.xfail("bar_comment_typing 失败")

    def btn_share_click(self):
        try:
            time.sleep(1)
            self.d(description="Share").click()
            time.sleep(1)

            from internal.infra.pages.spotfeed import SpotFeed
            return SpotFeed()

        except Exception as e:
            print(f"點擊 Share 失败: {e}")
            pytest.xfail("點擊 Share 失败")

    def bar_search_click(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').click()

        except Exception as e:
            print(f"bar_search_click 失败: {e}")
            pytest.xfail("bar_search_click 失败")

    def bar_search_typing(self):
        try:
            time.sleep(1)
            self.d.shell('input text "test"')

        except Exception as e:
            print(f"bar_search_typing 失败: {e}")
            pytest.xfail("bar_search_typing 失败")

    def screen_swipeupanddown(self):
        try:
            time.sleep(1)
            self.d.swipe_ext("up")

        except Exception as e:
            print(f"screen_swipeupanddown 失败: {e}")
            pytest.xfail("screen_swipeupanddown 失败")

    def list_result_community_click(self):
        try:
            time.sleep(5)
            self.d.click(*self.first_community_x_y)

        except Exception as e:
            print(f"list_result_community_click 失败: {e}")
            pytest.xfail("list_result_community_click 失败")

    def icon_message_click(self):
        try:
            time.sleep(3)
            self.d(description="M​e​s​s​a​g​e​s").click()
            time.sleep(3)

        except Exception as e:
            print(f"icon_message_click 失败: {e}")
            pytest.xfail("icon_message_click 失败")

    def icon_shareto_click(self):
        try:
            time.sleep(3)
            self.d(description="S​h​a​r​e​ ​t​o​.​.​.").click()
            time.sleep(3)

        except Exception as e:
            print(f"icon_shareto_click 失败: {e}")
            pytest.xfail("icon_shareto_click 失败")

    def icon_copylink_click(self):
        try:
            time.sleep(3)
            self.d(description="C​o​p​y​ ​L​i​n​k").click()
            time.sleep(3)

        except Exception as e:
            print(f"icon_copylink_click 失败: {e}")
            pytest.xfail("icon_copylink_click 失败")
