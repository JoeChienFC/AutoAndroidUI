import uiautomator2 as u2
import pytest
import os
import pytesseract
from PIL import Image
import time


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

    def is_not_on_gallery_page(self):
        if self.d(text="Photos").exists(timeout=3):
            pytest.fail("還在 gallery photos 頁面")

    def check_text_on_screen_ocr(self, text_to_find):
        """
        使用 OCR 檢查當前螢幕是否包含特定文字。
        """
        try:
            local_screenshot_path = "screen.png"  # 存到 Windows 本機
            time.sleep(1)
            # 截圖並儲存到 Android
            self.d.screenshot(local_screenshot_path)

            # 讀取圖片
            image = Image.open(local_screenshot_path)

            # OCR 識別
            ocr_text = pytesseract.image_to_string(image, lang="eng+chi_sim")  # 英文 + 簡體中文
            # 檢查是否包含指定文字
            if text_to_find in ocr_text:
                pass
            else:
                pytest.fail(f"OCR 找到的文字:{ocr_text} ，未找到題目要的文字: {text_to_find}")

        except Exception as e:
            print(f"OCR 檢查失敗: {e}")
            pytest.fail(f"OCR 檢查失敗: {e}")

        finally:
            # 清理本機端的截圖，避免累積
            if os.path.exists(local_screenshot_path):
                os.remove(local_screenshot_path)

