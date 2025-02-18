import uiautomator2 as u2
import time,pytest


class SetAsPopup:

    def __init__(self):
        self.d = u2.connect()
        self.share_image_popup_title = "Sharing image"

    def is_set_as_popup(self):
        if not self.d(text="Photos").exists and self.d(text="Wallpaper").exists:
            pytest.fail("沒有出現 Photos Wallpaper 合理推算沒有出現set as 彈窗")
