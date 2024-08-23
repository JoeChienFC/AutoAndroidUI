import uiautomator2 as u2
import time, pytest
import os


class GeneralPage:

    def __init__(self):
        self.btn_photos = "Photos"
        self.btn_albums = "Albums"
        self.btn_search = "Search"

        self.item_pic = ""
        self.item_video = ""
        self.btn_menu = ""

        self.d = u2.connect()

    def is_recent_app_page(self):
        if not self.d(resourceId="com.nothing.launcher:id/icon").exists(timeout=3):
            pytest.fail("沒有 gallery icon 不在最近頁面")

    def is_launcher_page(self):
        if not self.d(description="Home").exists(timeout=4):
            pytest.fail("沒有搜到 launcher 元件,代表不在桌面")

    def is_settings_page(self):
        if not self.d(resourceId="com.android.settings:id/homepage_title").exists(timeout=3):
            pytest.fail("不在設定頁面")

    def back(self):
        self.d.press('back')
        time.sleep(1)

    def btn_albums_click(self):
        self.d(description=self.btn_albums).click()
        time.sleep(1)

        from internal.infra.pages.albums_page import AlbumsPage
        return AlbumsPage()

    def btn_photos_click(self):
        self.d(description=self.btn_photos).click()
        time.sleep(1)

    def btn_search_click(self):
        self.d(description=self.btn_search).click()
        time.sleep(1)