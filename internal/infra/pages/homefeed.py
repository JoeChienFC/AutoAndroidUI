import uiautomator2 as u2
import time

from internal.infra.pages.communityfeed import CommunityFeed


class HOMEFeed:

    def __init__(self):
        self.d = u2.connect()

    def enter_community(self):

        try:
            if self.d(description="Tab 2 of 5").exists(5):
                self.d(description="Tab 2 of 5").click()
                print("成功进入community！")
                time.sleep(10)
                return CommunityFeed()
        except Exception as e:
            print(f"进入community失败: {e}")
            assert False, "进入community失败"
