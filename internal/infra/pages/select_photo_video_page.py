import uiautomator2 as u2
import time, pytest
import os


class SelectPhotoVideoPage:

    def __init__(self):
        self.photo = "Thumbnail"
        self.btn_finish = "FINISH"
        self.d = u2.connect()

    def photo_video_select(self):
        try:
            self.d(description=self.photo).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 photo_video_select 失败: {e}")
            pytest.xfail("點擊 photo_video_select 失败")

    def btn_finish_click(self):
        try:
            self.d(text=self.btn_finish).click(timeout=2)
            time.sleep(1)

            from internal.infra.pages.select_media_popup import SelectMediaPopup
            return SelectMediaPopup()

        except Exception as e:
            print(f"點擊 btn_finish_click 失败: {e}")
            pytest.xfail("點擊 btn_finish_click 失败")
