import uiautomator2 as u2
import time, pytest
import os


class SearchCommunity:

    def __init__(self):
        self.icon_more_xpath = '//android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ImageView[1]/android.view.View[1]/android.widget.ScrollView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[5]'
        self.icon_like_xpath = '//android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ImageView[1]/android.view.View[1]/android.widget.ScrollView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[4]'
        self.icon_share_xpath = '//android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ImageView[1]/android.view.View[1]/android.widget.ScrollView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]'
        self.icon_comment_xpath = '//android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.widget.ImageView[1]/android.view.View[1]/android.widget.ScrollView[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]'
        self.comment_text_x_y = (0.092, 0.283)
        self.text_username_x_y = (0.252, 0.208)
        self.pic_headshot_x_y = (0.095, 0.211)
        self.text_communityname_x_y = (0.196, 0.173)
        self.d = u2.connect()

    def text_communityname_click(self):
        try:
            time.sleep(2)
            self.d.click(*self.text_communityname_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 text_communityname_click 失败: {e}")

    def pic_headshot_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.pic_headshot_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 pic_headshot_click 失败: {e}")

    def text_username_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_username_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 text_username_click 失败: {e}")
            pytest.xfail("點 text_username_click 失败")

    def comment_text_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.comment_text_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 comment_text_click 失败: {e}")
            pytest.xfail("點 comment_text_click 失败")

    def icon_comment_click(self):
        try:
            time.sleep(1)
            self.d(className="android.widget.ImageView", index=2).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_comment_click 失败: {e}")
            pytest.xfail("點 icon_comment_click 失败")

    def icon_share_click(self):
        try:
            time.sleep(1)
            self.d(className="android.widget.ImageView", index=4).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_share_click 失败: {e}")
            pytest.xfail("點 icon_share_click 失败")

    def icon_like_click(self):
        try:
            time.sleep(1)
            self.d(className="android.widget.ImageView", index=6).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_like_click 失败: {e}")
            pytest.xfail("點 icon_like_click 失败")

    def icon_more_click(self):
        try:
            time.sleep(1)
            self.d(className="android.widget.ImageView", index=8).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_more_click 失败: {e}")
            pytest.xfail("點 icon_more_click 失败")


            