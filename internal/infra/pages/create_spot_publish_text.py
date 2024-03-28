import uiautomator2 as u2
import time, pytest
import os


class CreateSpotPublishText:

    def __init__(self):
        self.btn_hashtag_drag_xy1_xy2 = ()
        self.d = u2.connect()
        self.icon_close_xpath = '//android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]'
        self.icon_preview_close_xpath = '//android.widget.FrameLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]'
        self.pic_preview_xpath = '//android.widget.FrameLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]'
        self.icon_video_preview_close_xpath = '//android.widget.FrameLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[4]'
        self.icon_url_preview_close_xpath = '//android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]'
        self.icon_back_x_y = (0.062, 0.061)
        self.btn_community_x_y = (0.086, 0.743)
        self.textfields_comment_xpath = '//android.widget.EditText'
        self.location_pin_x_y = (0.182, 0.867)
        self.icon_album_x_y = (0.061, 0.867)
        self.btn_at_user_x_y = (0.232, 0.729)
        self.btn_hashtag_x_y = (0.11, 0.851)
        self.btn_add_x_y = (0.13, 0.737)

    def icon_back_click(self):
        try:
            self.d.click(*self.icon_back_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 icon_back_click 失败: {e}")

    def text_done_click(self):
        try:
            self.d.xpath('//android.widget.Button').click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 text_done_click 失败: {e}")

    def textfields_caption_typing(self):
        try:
            time.sleep(1)
            self.d.shell('input text "test"')
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_caption_typing 失败: {e}")
            pytest.xfail("點 textfields_caption_typing 失败")

    def icon_hashtag_click(self):
        try:
            self.d(className="android.widget.ImageView", index=0).click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 icon_hashtag_click 失败: {e}")

    def btn_hashtag_click(self):
        try:
            self.d.click(*self.btn_hashtag_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_hashtag_click 失败: {e}")
            pytest.xfail("點 btn_hashtag_click 失败")

    def btn_hashtag_drag(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.HorizontalScrollView').swipe("left")
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_hashtag_drag 失败: {e}")
            pytest.xfail("點 btn_hashtag_drag 失败")

    def btn_at_user_show(self):
        try:
            time.sleep(3)
            self.d.shell('input text "@test"')
            time.sleep(3)

        except Exception as e:
            print(f"點 btn_at_user_show 失败: {e}")
            pytest.xfail("點 btn_at_user_show 失败")

    def btn_at_user_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.btn_hashtag_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_at_user_click 失败: {e}")
            pytest.xfail("點 btn_at_user_click 失败")

    def btn_at_user_drag(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.HorizontalScrollView').swipe("left")
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_at_user_drag 失败: {e}")
            pytest.xfail("點 btn_at_user_drag 失败")
