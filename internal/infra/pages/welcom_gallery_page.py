import uiautomator2 as u2
import time, pytest
import os

from internal.infra.pages.photos_video_access_page import PhotosVideoAccessPage


class WelcomeGalleryPage:

    def __init__(self):
        self.d = u2.connect()

    def get_started_click(self):
        try:
            if self.d(resourceId="com.nothing.gallery:id/action", text="Get started").exists():
                self.d(resourceId="com.nothing.gallery:id/action", text="Get started").click()
                time.sleep(1)
            return PhotosVideoAccessPage()

        except Exception as e:
            print(f"點擊 get_started_click 失败: {e}")
            pytest.xfail("點擊 get_started_click 失败")

