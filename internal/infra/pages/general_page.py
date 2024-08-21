import uiautomator2 as u2
import time, pytest
import os


class GeneralPage:

    def __init__(self):
        self.btn_photos = ""
        self.btn_albums = ""
        self.btn_search = ""

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
