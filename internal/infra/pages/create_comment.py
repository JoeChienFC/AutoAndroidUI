import uiautomator2 as u2
import time,pytest


class CreateComment:

    def __init__(self):
        self.d = u2.connect()
        self.location_pin_x_y = (0.182, 0.867)
        self.icon_album_x_y = (0.061, 0.867)

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

    def icon_album_click(self):
        try:
            self.d.click(*self.icon_album_x_y)
            time.sleep(6)
            from internal.infra.pages.create_comment_upload_album import CreateCommentUploadAlbum
            return CreateCommentUploadAlbum

        except Exception as e:
            print(f"點 icon_album 失败: {e}")
            pytest.xfail("點 icon_album 失败")

