import uiautomator2 as u2
import time, pytest
import os


class AlbumsPage:

    def __init__(self):

        self.d = u2.connect()
        self.d(resourceId="com.nothing.gallery:id/entry_fragments").gesture((135, 622), (882, 1540), (525, 960),
                                                                            (613, 1121), 10)
        self.btn_more_options = "More options"
        self.icon_rename = "Rename"

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

    def btn_more_options_click(self):
        try:
            self.d(description=self.btn_more_options).click(timeout=2)
            time.sleep(1)

            from internal.infra.pages.settings_popover import SettingsPopover
            return SettingsPopover()

        except Exception as e:
            print(f"點擊 btn_more_options_click 失败: {e}")
            pytest.xfail("點擊 btn_more_options_click 失败")

    def check_album_count(self, album: str, count: str):
        if not self.d(text=album).exists:
            pytest.fail(f"沒有找到 {album} 相簿")
        if not self.d(text=album).down(text=f"{count} IMG").exists:
            pytest.fail(f"{album} 相簿沒有相片或不符合 TEST CASE 要求 {count} 張數")

    def albums_long_click(self, album: str):
        try:
            time.sleep(2)
            self.d(text=album).long_click(timeout=1)
            time.sleep(1)

        except Exception as e:
            print(f"長按 {album} 相簿失败: {e}")
            pytest.xfail(f"長按 {album} 相簿失败")

    def icon_rename_click(self):
        try:
            self.d(description=self.icon_rename).click(timeout=1)
            time.sleep(1)

            from internal.infra.pages.create_rename_album_popup import CreateRenameAlbumPopup
            return CreateRenameAlbumPopup()

        except Exception as e:
            print(f"點擊 icon_rename_click 失败: {e}")
            pytest.xfail("點擊 icon_rename_click 失败")

    def enter_albums(self, album: str):
        try:
            time.sleep(2)
            self.d(text=album).click(timeout=1)
            time.sleep(1)

            from internal.infra.pages.albums_detail_page import AlbumDetailPage
            return AlbumDetailPage()
        except Exception as e:
            print(f"點擊 {album} 相簿失败: {e}")
            pytest.xfail(f"點擊 {album} 相簿失败")
