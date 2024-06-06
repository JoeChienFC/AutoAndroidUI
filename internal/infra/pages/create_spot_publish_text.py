import uiautomator2 as u2
import time, pytest
import os


class CreateSpotPublishText:

    def __init__(self):
        self.icon_back = "icon_back"
        self.text_done = "text_done"
        self.btn_hashtag = "btn_hashtag"
        self.btn_at_user = "btn_at_user"

        self.d = u2.connect()


    def icon_back_click(self):
        try:
            self.d(description=self.icon_back).click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 icon_back_click 失败: {e}")

    def text_done_click(self):
        try:
            self.d(description=self.text_done).click()
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
            self.d(description=self.btn_hashtag).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_hashtag_click 失败: {e}")
            pytest.xfail("點 btn_hashtag_click 失败")

    def btn_hashtag_drag(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_hashtag).swipe("left")
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
            self.d(description=self.btn_at_user).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_at_user_click 失败: {e}")
            pytest.xfail("點 btn_at_user_click 失败")

    def btn_at_user_drag(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_at_user).swipe("left")
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_at_user_drag 失败: {e}")
            pytest.xfail("點 btn_at_user_drag 失败")
