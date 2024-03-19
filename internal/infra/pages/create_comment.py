import uiautomator2 as u2
import time, pytest


class CreateComment:

    def __init__(self):
        self.d = u2.connect()
        self.icon_close_xpath = '//android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]'
        self.icon_preview_close_xpath = '//android.widget.FrameLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]'
        self.pic_preview_xpath = '//android.widget.FrameLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]'
        self.icon_video_preview_close_xpath = '//android.widget.FrameLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[4]'
        self.icon_url_preview_close_xpath = '//android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]'
        self.icon_close_x_y = (0.925, 0.705)
        self.btn_community_x_y = (0.086, 0.743)
        self.textfields_comment_xpath = '//android.widget.EditText'
        self.location_pin_x_y = (0.182, 0.867)
        self.icon_album_x_y = (0.061, 0.867)
        self.btn_at_user_x_y = (0.232, 0.729)
        self.btn_hashtag_x_y = (0.232, 0.729)
        self.btn_add_x_y = (0.13, 0.737)
    def icon_close_click(self):
        try:
            self.d.click(*self.icon_close_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 icon_close 失败: {e}")

    def btn_community_click(self):
        try:
            self.d.click(*self.btn_community_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 btn_community 失败: {e}")

    def textfields_comment_click(self):
        try:
            self.d.xpath(self.textfields_comment_xpath).click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 textfields_comment 失败: {e}")

    def icon_location_pin_click(self):
        try:
            self.d.click(*self.location_pin_x_y)
            time.sleep(1)
            from internal.infra.pages.create_comment_location import CreateCommentLocation
            return CreateCommentLocation()

        except Exception as e:
            print(f"點 location_pin 失败: {e}")
            pytest.xfail("點 location_pin 失败")

    def btn_comment_click(self):
        try:
            self.d(description="Comment").click()
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_comment 失败: {e}")
            pytest.xfail("點 btn_comment 失败")

    def textfields_comment_typing(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').set_text("test")
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_comment_typing 失败: {e}")
            pytest.xfail("點 textfields_comment_typing 失败")

    def textfields_comment_typing_at_user(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').set_text("@te")
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_comment_typing_at_user 失败: {e}")
            pytest.xfail("點 textfields_comment_typing_at_user 失败")

    def textfields_comment_typing_hashtag(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').set_text("#te")
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_comment_typing_hashtag 失败: {e}")
            pytest.xfail("點 textfields_comment_typing_hashtag 失败")

    def icon_album_click(self):
        try:
            self.d.click(*self.icon_album_x_y)
            time.sleep(6)
            from internal.infra.pages.create_comment_upload_album import CreateCommentUploadAlbum
            return CreateCommentUploadAlbum

        except Exception as e:
            print(f"點 icon_album 失败: {e}")
            pytest.xfail("點 icon_album 失败")

    def btn_at_user_drag(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.HorizontalScrollView').swipe("left")
            time.sleep(1)

        except Exception as e:
            print(f"點 at_user_drag 失败: {e}")
            pytest.xfail("點 at_user_drag 失败")

    def btn_at_user_click(self):
        try:
            self.d.click(*self.btn_at_user_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 at_user_drag 失败: {e}")
            pytest.xfail("點 at_user_drag 失败")

    def btn_hashtag_drag(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.HorizontalScrollView').swipe("left")
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_hashtag_drag 失败: {e}")
            pytest.xfail("點 btn_hashtag_drag 失败")

    def btn_hashtag_click(self):
        try:
            self.d.click(*self.btn_hashtag_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_hashtag 失败: {e}")
            pytest.xfail("點 btn_hashtag 失败")

    def pic_preview_drag(self):
        try:
            time.sleep(1)
            self.d.xpath(self.pic_preview_xpath).swipe("left")
            time.sleep(1)

        except Exception as e:
            print(f"點 pic_preview_drag 失败: {e}")
            pytest.xfail("點 pic_preview_drag 失败")

    def icon_preview_close_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.icon_preview_close_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_preview_close 失败: {e}")
            pytest.xfail("點 icon_preview_close 失败")

    def icon_video_preview_close_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.icon_video_preview_close_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_preview_close 失败: {e}")
            pytest.xfail("點 icon_preview_close 失败")

    def comment_url_typing(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').set_text("https://www.google.com")
            time.sleep(1)

        except Exception as e:
            print(f"點 comment_url_typing 失败: {e}")
            pytest.xfail("點 comment_url_typing 失败")

    def icon_url_preview_close_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.icon_url_preview_close_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_url_preview_close 失败: {e}")
            pytest.xfail("點 icon_url_preview_close 失败")

    def btn_add_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.btn_add_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_add 失败: {e}")
            pytest.xfail("點 btn_add 失败")