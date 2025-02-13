import uiautomator2 as u2
import time, pytest
import os


class AlbumsPage:

    def __init__(self):

        self.d = u2.connect()
        self.d(resourceId="com.nothing.gallery:id/entry_fragments").gesture((135, 622), (882, 1540), (525, 960),
                                                                            (613, 1121), 10)

    def is_favourite_album(self):
        if not self.d(resourceId="com.nothing.gallery:id/display_name", text="Favourite").exists(timeout=2):
            pytest.fail("沒有 Favourite 相簿")

    def check_favorites_album_photos_count(self, count=str):
        img = self.d(resourceId="com.nothing.gallery:id/display_name", text="Favourite").down(
            resourceId="com.nothing.gallery:id/photo_media_count", text=f"{count} IMG")
        if not img:
            pytest.fail(f"Favourite 相簿沒有相片或不符合TEST CASE 要求 {count} 張數")

    def check_favorites_album_video_count(self, count=str):
        img = self.d(resourceId="com.nothing.gallery:id/display_name", text="Favourite").down(
            resourceId="com.nothing.gallery:id/video_media_count", text=f"{count} VID")
        if not img:
            pytest.fail(f"Favourite 相簿沒有 video 或不符合TEST CASE 要求 {count} 數量")

    def check_recently_deleted_album_photos_count(self, count=str):
        img = self.d(resourceId="com.nothing.gallery:id/display_name", text="Recently deleted").down(
            resourceId="com.nothing.gallery:id/photo_media_count", text=f"{count} IMG")
        if not img:
            pytest.fail(f"Recently 相簿沒有相片或不符合TEST CASE 要求 {count} 張數")

    def check_recently_deleted_album_video_count(self, count=str):
        img = self.d(resourceId="com.nothing.gallery:id/display_name", text="Recently deleted").down(
            resourceId="com.nothing.gallery:id/video_media_count", text=f"{count} VID")
        if not img:
            pytest.fail(f"Recently 相簿沒有 video 或不符合TEST CASE 要求 {count} 張數")

    def check_data_album_count(self, count=str):
        img = self.d(resourceId="com.nothing.gallery:id/display_name", text="data_albums").down(
            resourceId="com.nothing.gallery:id/photo_media_count", text=f"{count} IMG")
        if not img:
            pytest.fail(f"data_album 相簿沒有相片或不符合 TEST CASE 要求 {count} 張數")

    def check_data_album_video_count(self, count=str):
        img = self.d(resourceId="com.nothing.gallery:id/display_name", text="data_albums").down(
            resourceId="com.nothing.gallery:id/video_media_count", text=f"{count} VID")
        if not img:
            pytest.fail(f"data_album 相簿沒有 video 或不符合 TEST CASE 要求 {count} 張數")

    def check_camera_photo_count(self, count=str):
        img = self.d(resourceId="com.nothing.gallery:id/display_name", text="Camera").down(
            resourceId="com.nothing.gallery:id/photo_media_count", text=f"{count} IMG")
        if not img:
            pytest.fail(f"Camera 相簿沒有不符合 TEST CASE 要求 {count} 張數")

    def check_camera_video_count(self, count=str):
        img = self.d(resourceId="com.nothing.gallery:id/display_name", text="Camera").down(
            resourceId="com.nothing.gallery:id/video_media_count", text=f"{count} VID")
        if not img:
            pytest.fail(f"Camera 相簿沒有 video 或不符合 TEST CASE 要求 {count} 張數")

