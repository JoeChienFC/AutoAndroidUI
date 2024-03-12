import uiautomator2 as u2
import time


class BottomTab:

    def __init__(self):
        self.d = u2.connect()

    def bottomtab_myprofile_click(self):
        try:
            if self.d(description="Tab 5 of 5").exists(5):
                self.d(description="Tab 5 of 5").click()
                print("成功進入 myprofile！")
                time.sleep(2)
                from internal.infra.pages.myprofile import MyProfile
                return MyProfile()
            else:
                assert False, "進入 myprofile 失败"
        except Exception as e:
            print(f"進入 myprofile 失败: {e}")
            assert False, "進入 myprofile 失败"

    def bottomtab_explore_click(self):
        try:
            if self.d(description="Tab 4 of 5").exists(5):
                self.d(description="Tab 4 of 5").click()
                print("成功進入 explore！")

        except Exception as e:
            print(f"進入 explore 失败: {e}")
            assert False, "進入 explore 失败"

    def bottomtab_ai_click(self):
        try:
            if self.d(description="Tab 3 of 5").exists(5):
                self.d(description="Tab 3 of 5").click()
                print("成功進入ai！")
                time.sleep(2)

        except Exception as e:
            print(f"進入 ai 失败: {e}")
            assert False, "進入 ai 失败"

    def bottomtab_spot_click(self):
        try:
            if self.d(description="Tab 2 of 5").exists(5):
                self.d(description="Tab 2 of 5").click()
                print("成功進入spot！")
                time.sleep(2)
                from internal.infra.pages.homefeed import HomeFeed
                return HomeFeed()
        except Exception as e:
            print(f"進入spot失败: {e}")
            assert False, "進入spot失败"

    def bottomtab_community_click(self):
        try:
            if self.d(description="Tab 1 of 5").exists(5):
                self.d(description="Tab 1 of 5").click()
                print("成功進入community！")
                time.sleep(2)
                from internal.infra.pages.homefeed import HomeFeed
                return HomeFeed()
        except Exception as e:
            print(f"進入 community 失败: {e}")
            assert False, "進入 community 失败"

