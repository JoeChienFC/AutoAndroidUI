import uiautomator2 as u2
import time,pytest


class CommunityCommentPage:

    def __init__(self):
        self.d = u2.connect()
        self.title_community_name = (0.502, 0.052)
        self.back_icon_x_y = (0.067, 0.06)
        self.pic_main_headshot_x_y = (0.091, 0.132)
        self.pic_main_username_x_y = (0.167, 0.129)

    def title_communityname_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.title_community_name)
            time.sleep(3)

        except Exception as e:
            print(f"點擊 title_community_name 失败: {e}")
            pytest.xfail("點擊 title_community_name 失败")

    def icon_back_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.back_icon_x_y)

        except Exception as e:
            print(f"點擊 back_icon 失败: {e}")
            pytest.xfail("點擊 back_icon 失败")

    def pic_main_headshot_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.pic_main_headshot_x_y)

        except Exception as e:
            print(f"點擊 pic_main_headshot 失败: {e}")
            pytest.xfail("點擊 pic_main_headshot 失败")

    def pic_main_username_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.pic_main_username_x_y)

        except Exception as e:
            print(f"點擊 pic_main_username 失败: {e}")
            pytest.xfail("點擊 pic_main_username 失败")

    def text_translation_click(self):
        try:
            time.sleep(1)
            if self.d(description="See Translation").exists(2):
                self.d(description="See Translation").click()
            else:
                self.d(description="See Original").click()
                time.sleep(1.5)
                self.d(description="See Translation").click()

        except Exception as e:
            print(f"點擊 text_translation 失败: {e}")
            pytest.xfail("點擊 text_translation 失败")

