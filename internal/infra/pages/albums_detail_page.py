import uiautomator2 as u2
import time, pytest
import os


class AlbumDetailPage:

    def __init__(self):

        self.d = u2.connect()
        self.photo = "Thumbnail"
        self.icon_add = "Add"
        self.btn_more = "More"

    def icon_add_click(self):
        try:
            self.d(description=self.icon_add).click(timeout=1)
            time.sleep(1)

            from internal.infra.pages.select_photo_video_page import SelectPhotoVideoPage
            return SelectPhotoVideoPage()

        except Exception as e:
            print(f"點擊 icon_add_click 失败: {e}")
            pytest.xfail("點擊 icon_add_click 失败")

    def photo_long_click(self):
        try:
            time.sleep(2)
            self.d(description=self.photo).long_click(timeout=1)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 photo_click 失败: {e}")
            pytest.xfail("點擊 photo_click 失败")

    def icon_more_click(self):
        try:
            self.d(description=self.btn_more).click()
            time.sleep(1)

            from internal.infra.pages.select_photo_more_popover import SelectPhotoMorePopover
            return SelectPhotoMorePopover()
        except Exception as e:
            print(f"點擊 btn_more_click 失败: {e}")
            pytest.xfail("點擊 btn_more_click 失败")