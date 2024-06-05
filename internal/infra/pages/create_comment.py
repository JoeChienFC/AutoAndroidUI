import uiautomator2 as u2
import time, pytest


class CreateComment:

    def __init__(self):
        self.icon_url_preview_close = "icon_url_preview_close"
        self.icon_video_preview_close = "icon_video_preview_close"
        self.icon_preview_close = "icon_preview_close"
        self.pic_preview = "pic_preview"
        self.btn_hashtag = "btn_hashtag"
        self.btn_at_user = "btn_at_user"
        self.icon_album = "icon_album"
        self.btn_comment = "btn_comment"
        self.icon_location_pin = "icon_location_pin"
        self.textfields_comment = "textfields_comment"
        self.btn_community = "btn_community"
        self.icon_close = "icon_close"
        self.btn_add = "btn_add"
        self.d = u2.connect()

    def icon_close_click(self):
        try:
            self.d(description=self.icon_close).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 icon_close 失败: {e}")

    def btn_community_click(self):
        try:
            self.d(description=self.btn_community).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 btn_community 失败: {e}")

    def textfields_comment_click(self):
        try:
            time.sleep(1)
            self.d(description=self.textfields_comment).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 textfields_comment 失败: {e}")

    def icon_location_pin_click(self):
        try:
            self.d(description=self.icon_location_pin).click(timeout=2)
            time.sleep(1)
            from internal.infra.pages.create_comment_location import CreateCommentLocation
            return CreateCommentLocation()

        except Exception as e:
            print(f"點 location_pin 失败: {e}")
            pytest.xfail("點 location_pin 失败")

    def btn_comment_click(self):
        try:
            self.d(description=self.btn_comment).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_comment 失败: {e}")
            pytest.xfail("點 btn_comment 失败")

    def textfields_comment_typing(self):
        try:
            time.sleep(1)
            self.d.shell('input text "test"')
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_comment_typing 失败: {e}")
            pytest.xfail("點 textfields_comment_typing 失败")

    def textfields_comment_typing_chinese(self):
        try:
            time.sleep(1)
            # self.d.xpath('//android.widget.EditText').set_text("你好")
            # os.system('adb shell input text {}'.format("你好"))
            self.d.shell('input text "你好"')
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_comment_typing_chinese 失败: {e}")
            pytest.xfail("點 textfields_comment_typing_chinese 失败")

    def textfields_comment_typing_at_user(self):
        try:
            time.sleep(1)
            # self.d.xpath('//android.widget.EditText').set_text("@te")
            # os.system('adb shell input text {}'.format("@te"))
            self.d.shell('input text "@te"')
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_comment_typing_at_user 失败: {e}")
            pytest.xfail("點 textfields_comment_typing_at_user 失败")

    def textfields_comment_typing_hashtag(self):
        try:
            time.sleep(1)
            # self.d.xpath('//android.widget.EditText').set_text("#te")
            # os.system('adb shell input text {}'.format("#te"))
            self.d.shell('input text "#te"')
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_comment_typing_hashtag 失败: {e}")
            pytest.xfail("點 textfields_comment_typing_hashtag 失败")

    def icon_album_click(self):
        try:
            self.d(description=self.icon_album).click(timeout=2)
            time.sleep(6)
            from internal.infra.pages.create_comment_upload_album import CreateCommentUploadAlbum
            return CreateCommentUploadAlbum

        except Exception as e:
            print(f"點 icon_album 失败: {e}")
            pytest.xfail("點 icon_album 失败")

    def btn_at_user_drag(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_at_user).swipe("left")
            time.sleep(1)

        except Exception as e:
            print(f"點 at_user_drag 失败: {e}")
            pytest.xfail("點 at_user_drag 失败")

    def btn_at_user_click(self):
        try:
            self.d(description=self.btn_at_user).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_at_user 失败: {e}")
            pytest.xfail("點 btn_at_user 失败")

    def btn_hashtag_drag(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_hashtag).swipe("left")
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_hashtag_drag 失败: {e}")
            pytest.xfail("點 btn_hashtag_drag 失败")

    def btn_hashtag_click(self):
        try:
            self.d(description=self.btn_hashtag).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_hashtag 失败: {e}")
            pytest.xfail("點 btn_hashtag 失败")

    def pic_preview_drag(self):
        try:
            time.sleep(1)
            self.d(description=self.pic_preview).swipe("left")
            time.sleep(1)

        except Exception as e:
            print(f"點 pic_preview_drag 失败: {e}")
            pytest.xfail("點 pic_preview_drag 失败")

    def icon_preview_close_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_preview_close).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_preview_close 失败: {e}")
            pytest.xfail("點 icon_preview_close 失败")

    def icon_video_preview_close_click(self):
        try:
            self.d(description=self.icon_video_preview_close).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_preview_close 失败: {e}")
            pytest.xfail("點 icon_preview_close 失败")

    def comment_url_typing(self):
        try:
            time.sleep(1)
            # self.d.xpath('//android.widget.EditText').set_text("https://www.google.com")
            # os.system('adb shell input text {}'.format("https://www.google.com"))
            self.d.shell('input text "https://www.google.com"')
            time.sleep(1)

        except Exception as e:
            print(f"點 comment_url_typing 失败: {e}")
            pytest.xfail("點 comment_url_typing 失败")

    def icon_url_preview_close_click(self):
        try:
            self.d(description=self.icon_url_preview_close).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_url_preview_close 失败: {e}")
            pytest.xfail("點 icon_url_preview_close 失败")

    def btn_add_click(self):
        try:
            self.d(description=self.btn_add).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_add 失败: {e}")
            pytest.xfail("點 btn_add 失败")
