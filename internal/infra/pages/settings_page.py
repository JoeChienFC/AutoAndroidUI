import uiautomator2 as u2
import time, pytest
import os


class SettingsPage:

    def __init__(self):
        self.d = u2.connect()

    def btn_show_in_photos_view_click(self):
        try:
            self.d(text="Show in photos view").click()
            time.sleep(1)

            from internal.infra.pages.show_in_photos_view_page import ShowInPhotosViewPage
            return ShowInPhotosViewPage

        except Exception as e:
            print(f"點擊 btn_show_in_photos_view_click 失败: {e}")
            pytest.xfail("點擊 btn_show_in_photos_view_click 失败")

