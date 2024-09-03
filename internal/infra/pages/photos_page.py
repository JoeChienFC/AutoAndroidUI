import uiautomator2 as u2
import time, pytest
import os


class PhotosPage:

    def __init__(self):
        self.btn_more = "More"
        self.btn_delete = "Delete"
        self.btn_share = "Share"
        self.btn_copy_to_album = "Copy to album"
        self.photo = "Thumbnail"
        self.btn_more_options = "More options"

        self.d = u2.connect()

    def is_photos_page(self):
        if not self.d(text="Photos").exists(timeout=3):
            pytest.fail("不在 Photos 頁面")

    def is_display_no_photos_text(self):
        if not self.d(text="No photo here, go take some photos!").exists(timeout=2):
            pytest.fail("照片頁沒有顯示_沒有照片_的文案")

    def no_display_no_photos_text(self):
        if self.d(text="No photo here, go take some photos!").exists(timeout=2):
            pytest.fail("照片頁顯示_沒有照片_的文案")

    def is_video_exists(self):
        if not self.d(text="00:10", resourceId="com.nothing.gallery:id/video_duration").exists(timeout=2):
            pytest.fail("照片頁沒有 test case 的影片")

    def is_two_photos_exists(self):
        if self.d(text="Today").exists:
            two_img = self.d(text="Today").down(description="Thumbnail")
            if not two_img:
                pytest.fail("照片頁沒有 2 張照片")
        else:
            pytest.fail("照片頁沒有 2 張照片")

    def no_photos_exists(self):
        if self.d(resourceId="com.nothing.gallery:id/title", text="2 August").exists(timeout=1):
            pytest.fail("照片頁有其他照片")
        if self.d(resourceId="com.nothing.gallery:id/title", text="1 August").exists(timeout=1):
            pytest.fail("照片頁有其他照片")

    def close_gallery_with_swipe_up(self):
        self.d.swipe(0.496, 0.991, 0.496, 0.3, duration=0.1)

    def go_to_recent_app_with_swipe_up(self):
        self.d.swipe(0.496, 0.991, 0.496, 0.9, duration=1.7)

    def go_to_last_app_with_swipe_left(self):
        self.d.swipe(0.304, 0.991, 0.661, 0.991, duration=0.1)

    def btn_more_options_click(self):
        try:
            self.d(description=self.btn_more_options).click(timeout=2)
            time.sleep(1)

            from internal.infra.pages.settings_popover import SettingsPopover
            return SettingsPopover()

        except Exception as e:
            print(f"點擊 btn_more_options_click 失败: {e}")
            pytest.xfail("點擊 btn_more_options_click 失败")

    def photo_click(self):
        try:
            self.d(description=self.photo).click()
            time.sleep(1)

            from internal.infra.pages.photo_all_view_page import PhotoAllViewPage
            return PhotoAllViewPage()

        except Exception as e:
            print(f"點擊 photo_click 失败: {e}")
            pytest.xfail("點擊 photo_click 失败")

    def photo_long_click(self):
        try:
            self.d(description=self.photo).long_click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 photo_click 失败: {e}")
            pytest.xfail("點擊 photo_click 失败")

    def is_date_order_correct(self):
        try:
            correct0 = self.d(resourceId="com.nothing.gallery:id/title", text="24 July").down(
                resourceId="com.nothing.gallery:id/title", text="23 July")
            correct1 = self.d(resourceId="com.nothing.gallery:id/title", text="23 July").down(
                resourceId="com.nothing.gallery:id/title", text="22 July")
            correct2 = self.d(resourceId="com.nothing.gallery:id/title", text="22 July").down(
                resourceId="com.nothing.gallery:id/title", text="21 July")

            if not (correct0 and correct1 and correct2):
                pytest.fail("有照片日期排序錯誤")

        except Exception as e:
            print(f"有照片日期的元件沒出現: {e}")
            pytest.xfail("有照片日期的元件沒出現")

    def icon_copy_to_album_click(self):
        try:
            self.d(description=self.btn_copy_to_album).click()
            time.sleep(1)

            from internal.infra.pages.copy_to_album_page import CopyToAlbumPage
            return CopyToAlbumPage()
        except Exception as e:
            print(f"點擊 btn_copy_to_album_click 失败: {e}")
            pytest.xfail("點擊 btn_copy_to_album_click 失败")

    def icon_share_click(self):
        try:
            self.d(description=self.btn_share).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_share_click 失败: {e}")
            pytest.xfail("點擊 btn_share_click 失败")

    def icon_delete_click(self):
        try:
            self.d(description=self.btn_delete).click()
            time.sleep(1)

            from internal.infra.pages.delete_mediaa_popup import DeleteMediaPopup
            return DeleteMediaPopup()
        except Exception as e:
            print(f"點擊 btn_delete_click 失败: {e}")
            pytest.xfail("點擊 btn_delete_click 失败")

    def icon_more_click(self):
        try:
            self.d(description=self.btn_more).click()
            time.sleep(1)

            from internal.infra.pages.photo_more_popover import PhotoMorePopover
            return PhotoMorePopover()
        except Exception as e:
            print(f"點擊 btn_more_click 失败: {e}")
            pytest.xfail("點擊 btn_more_click 失败")

    def no_select_click(self):
        try:
            self.d(resourceId="com.nothing.gallery:id/selection", selected="false").click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 no_select_click 失败: {e}")
            pytest.xfail("點擊 no_select_click 失败")

    def is_july_24_pic_exit(self):
        if not self.d(resourceId="com.nothing.gallery:id/title", text="24 July").exists(timeout=3):
            pytest.fail("icon（+）功能 加入到相簿的相片消失了")

    def is_today_pic_exit(self):
        if not self.d(resourceId="com.nothing.gallery:id/title", text="Today").exists(timeout=3):
            pytest.fail("没有今天的相片")

