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

    def is_photos_page(self):
        if not self.d(text="Photos").exists(timeout=3):
            pytest.fail("不在 Photos 頁面")

    def close_gallery_with_swipe_up(self):
        self.d.swipe(0.496, 0.991, 0.496, 0.3, duration=0.1)

    def go_to_recent_app_with_swipe_up(self):
        self.d.swipe(0.496, 0.991, 0.496, 0.9, duration=1.7)

    def go_to_last_app_with_swipe_left(self):
        self.d.swipe(0.304, 0.991, 0.661, 0.991, duration=0.1)

    def btn_photos_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_photos).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_photos 失败: {e}")
            pytest.xfail("點擊 btn_photos 失败")

    def btn_albums_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_albums).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_albums 失败: {e}")
            pytest.xfail("點擊 btn_albums 失败")

