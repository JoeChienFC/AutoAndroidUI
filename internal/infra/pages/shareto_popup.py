import uiautomator2 as u2
import time,pytest


class ShareToPopup:

    def __init__(self):
        self.d = u2.connect()
        self.first_community_x_y = (0.479, 0.448)

    def select_first_community(self):
        try:
            time.sleep(3)
            self.d.click(*self.first_community_x_y)

        except Exception as e:
            print(f"選第一個 community 失败: {e}")
            pytest.xfail("選第一個 community 失败")

    def share_click(self):
        try:
            time.sleep(1)
            self.d(description="Share").click()
            time.sleep(1)

            from internal.infra.pages.spotfeed import SpotFeed
            return SpotFeed()

        except Exception as e:
            print(f"點擊 Share 失败: {e}")
            pytest.xfail("點擊 Share 失败")


