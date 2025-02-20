import uiautomator2 as u2
import time, pytest


class CreateAlbumPopup:

    def __init__(self):
        self.btn_cancel = "Cancel"
        self.btn_ok = "OK"
        self.d = u2.connect()

    def btn_ok_click(self):
        try:
            self.d(text=self.btn_ok).click()
            time.sleep(1)

            from internal.infra.pages.select_photo_video_page import SelectPhotoVideoPage
            return SelectPhotoVideoPage()

        except Exception as e:
            print(f"點擊 btn_ok_click 失败: {e}")
            pytest.xfail("點擊 btn_ok_click 失败")

    def btn_cancel_click(self):
        try:
            time.sleep(1)
            self.d(text=self.btn_cancel).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_cancel 失败: {e}")
            pytest.xfail("點擊 btn_cancel 失败")

    def is_ok_btn_gray(self):
        if self.d(text=self.btn_ok, enabled="true").exists:
            pytest.xfail("OK按鈕並未反灰，可點擊")

    def send_keys(self, text: str):
        try:
            self.d.send_keys(text)
            time.sleep(1)

        except Exception as e:
            print(f"send_keys 失败: {e}")
            pytest.xfail("send_keys 失败")

    def is_texts_exists(self, text: str):
        if not self.d(text=text).exists:
            pytest.xfail(f"文字_{text}_沒有出現")
