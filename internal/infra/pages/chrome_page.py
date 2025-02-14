import uiautomator2 as u2
import time, pytest
import os


class ChromePage:

    def __init__(self):
        self.d = u2.connect()
        if self.d(text="Use without an account").exists(timeout=1):
            self.d(text="Use without an account").click()
        if self.d(text="No, thanks").exists(timeout=1):
            self.d(text="No, thanks").click()

    def is_gallery_info_html(self):
        if not self.d(text="Terms of Service for Gallery").exists(timeout=3):
            pytest.fail("沒有找到 gallery info html 關鍵字")

