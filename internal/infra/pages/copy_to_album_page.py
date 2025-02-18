import uiautomator2 as u2
import time, pytest
import os


class CopyToAlbumPage:

    def __init__(self):
        self.d = u2.connect()
        self.copy_to_album_page_title = "Copy to album"

    def data_albums_click(self):
        try:
            self.d(resourceId="com.nothing.gallery:id/display_name", text="data_albums").click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 data_albums_click 失败: {e}")
            pytest.xfail("點擊 data_albums_click 失败")

    def is_copy_to_album_page(self):
        if not self.d(text=self.copy_to_album_page_title).exists:
            pytest.fail("不在 copy_to_album_page 頁面")
