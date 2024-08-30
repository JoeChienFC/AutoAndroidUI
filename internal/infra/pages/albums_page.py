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

    def is_recently_deleted_album_has_1_img(self):
        img = self.d(resourceId="com.nothing.gallery:id/display_name", text="Recently deleted").down(
            resourceId="com.nothing.gallery:id/photo_media_count", text="1 IMG")
        if not img:
            pytest.fail("Recently 相簿沒有相片或不符合TEST CASE 張數")

    def is_recently_deleted_album_has_2_img(self):
        img = self.d(resourceId="com.nothing.gallery:id/display_name", text="Recently deleted").down(
            resourceId="com.nothing.gallery:id/photo_media_count", text="2 IMG")
        if not img:
            pytest.fail("Recently 相簿沒有相片或不符合TEST CASE 張數")

    def is_data_album_has_6_img(self):
        img = self.d(resourceId="com.nothing.gallery:id/display_name", text="data_albums").down(
            resourceId="com.nothing.gallery:id/photo_media_count", text="6 IMG")
        if not img:
            pytest.fail("data_album 相簿沒有相片或不符合 TEST CASE 張數")

    def is_data_album_has_7_img(self):
        img = self.d(resourceId="com.nothing.gallery:id/display_name", text="data_albums").down(
            resourceId="com.nothing.gallery:id/photo_media_count", text="7 IMG")
        if not img:
            pytest.fail("data_album 相簿沒有相片或不符合 TEST CASE 張數")

