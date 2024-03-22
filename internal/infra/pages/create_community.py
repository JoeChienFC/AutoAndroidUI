import uiautomator2 as u2
import time, pytest


class CreateCommunity:

    def __init__(self):
        self.textfields_communityname_x_y = None
        self.btn_edit_photo_x_y = None
        self.icon_back_x_y = None
        self.d = u2.connect()
        
    def icon_back_click(self):
        try:
            self.d.click(*self.icon_back_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 icon_back_click 失败: {e}")

    def btn_edit_photo_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.btn_edit_photo_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 btn_edit_photo_click 失败: {e}")

    def textfields_communityname_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.textfields_communityname_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 textfields_communityname_click 失败: {e}")

    def textfields_communityname_typing(self):
        try:
            self.d.click(*self.location_pin_x_y)
            time.sleep(1)
            from internal.infra.pages.create_comment_location import CreateCommentLocation
            return CreateCommentLocation()

        except Exception as e:
            print(f"點 location_pin 失败: {e}")
            pytest.xfail("點 location_pin 失败")

    def textbar_location_click(self):
        try:
            self.d(description="Comment").click()
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_comment 失败: {e}")
            pytest.xfail("點 btn_comment 失败")

    def textfields_description_click(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').set_text("test")
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_comment_typing 失败: {e}")
            pytest.xfail("點 textfields_comment_typing 失败")

    def textfields_description_typing(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').set_text("你好")
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_comment_typing_chinese 失败: {e}")
            pytest.xfail("點 textfields_comment_typing_chinese 失败")

    def btn_create_click(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').set_text("@te")
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_comment_typing_at_user 失败: {e}")
            pytest.xfail("點 textfields_comment_typing_at_user 失败")

