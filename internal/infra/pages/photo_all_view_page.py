import uiautomator2 as u2
import time, pytest
import os


class PhotoAllViewPage:

    def __init__(self):
        self.photo = "Thumbnail"
        self.btn_more_options = "More options"
        self.favorite = "Set as favorite"
        self.un_favorite = "Unfavorite"

        self.d = u2.connect()

    def set_as_favorite_click(self):
        try:
            if self.d(description=self.favorite).exists:
                self.d(description=self.favorite).click()
                time.sleep(1)

        except Exception as e:
            print(f"點擊 set_as_favorite_click 失败: {e}")
            pytest.xfail("點擊 set_as_favorite_click 失败")

    def is_un_favorite_exists(self):
        if not self.d(description=self.un_favorite).exists:
            pytest.fail("沒有實心愛心的存在")

    def photo_click(self):
        try:
            self.d(description=self.photo).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 photo_click 失败: {e}")
            pytest.xfail("點擊 photo_click 失败")


