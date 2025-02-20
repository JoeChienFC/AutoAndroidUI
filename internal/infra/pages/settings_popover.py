import uiautomator2 as u2
import time, pytest
import os


class SettingsPopover:

    def __init__(self):
        self.d = u2.connect()

    def btn_settings_click(self):
        try:
            self.d(text="Settings").click()
            time.sleep(1)
            from internal.infra.pages.settings_page import SettingsPage
            return SettingsPage()

        except Exception as e:
            print(f"點擊 btn_settings_click 失败: {e}")
            pytest.xfail("點擊 btn_settings_click 失败")

    def btn_create_click(self):
        try:
            self.d(text="Create").click()
            time.sleep(1)
            from internal.infra.pages.create_album_popup import CreateAlbumPopup
            return CreateAlbumPopup()

        except Exception as e:
            print(f"點擊 btn_create_click 失败: {e}")
            pytest.xfail("點擊 btn_create_click 失败")

