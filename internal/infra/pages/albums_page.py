import uiautomator2 as u2
import time, pytest
import os


class AlbumsPage:

    def __init__(self):

        self.d = u2.connect()

    def is_favorite_album(self):
        if not self.d(resourceId="com.nothing.gallery:id/display_name", text="Favorite").exists(timeout=2):
            pytest.fail("沒有 Favorite 相簿")

    def is_favorite_album_has_1_img(self):
        img = self.d(resourceId="com.nothing.gallery:id/display_name", text="Favorite").down(
            resourceId="com.nothing.gallery:id/photo_media_count", text="1 IMG")
        if not img:
            pytest.fail("Favorite 相簿沒有相片或不符合TEST CASE 張數")
