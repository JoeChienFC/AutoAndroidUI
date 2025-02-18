import uiautomator2 as u2
import time,pytest


class ShareImagePopup:

    def __init__(self):
        self.d = u2.connect()
        self.share_image_popup_title = "Sharing image"

    def is_share_image_popup(self):
        if not self.d(text=self.share_image_popup_title).exists:
            pytest.fail("沒有出現 share image 彈框")
