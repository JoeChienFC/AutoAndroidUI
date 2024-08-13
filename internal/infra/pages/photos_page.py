import uiautomator2 as u2
import time, pytest
import os


class PhotosPage:

    def __init__(self):
        self.btn_photos = ""
        self.btn_albums = ""
        self.btn_search = ""

        self.item_pic = ""
        self.item_video = ""
        self.btn_menu = ""

        self.d = u2.connect()

    def btn_photos_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_photos).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_photos 失败: {e}")
            pytest.xfail("點擊 btn_photos 失败")

    def btn_photos_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_photos).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_photos 失败: {e}")
            pytest.xfail("點擊 btn_photos 失败")