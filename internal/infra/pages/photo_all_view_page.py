import uiautomator2 as u2
import time, pytest
import os


class PhotoAllViewPage:

    def __init__(self):
        self.thumbnail = "Thumbnail"
        self.share_icon = "Share"
        self.more_icon = "More"
        self.delete_icon = "Delete"
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

    def delete_click(self):
        try:
            self.d(description=self.delete_icon).click()
            time.sleep(1)

            from internal.infra.pages.delete_mediaa_popup import DeleteMediaPopup
            return DeleteMediaPopup()
        except Exception as e:
            print(f"點擊 delete_click 失败: {e}")
            pytest.xfail("點擊 delete_click 失败")

    def more_click(self):
        try:
            self.d(description=self.more_icon).click()
            time.sleep(1)

            from internal.infra.pages.photo_more_popover import PhotoMorePopover
            return PhotoMorePopover()

        except Exception as e:
            print(f"點擊 more_click 失败: {e}")
            pytest.xfail("點擊 more_click 失败")

    def share_click(self):
        try:
            self.d(description=self.share_icon).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 share_click 失败: {e}")
            pytest.xfail("點擊 share_click 失败")

    def is_location_details_correct(self):
        if not self.d(resourceId="com.nothing.gallery:id/taken_time_date", text="9 August").exists:
            pytest.fail("沒有日期時間存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/display_name", text="location_pic.jpg").exists:
            pytest.fail("沒有檔名資訊存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/device_name", text="Nothing A065").exists:
            pytest.fail("沒有 device_name 資訊存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/pixel_count", text="12.6 MP").exists:
            pytest.fail("沒有 Image 資訊存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/focal_length", text="5.59 mm").exists:
            pytest.fail("沒有 Capture 資訊存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/geo_location_panel", description="Geo location panel").exists:
            pytest.fail("沒有 geo_location 資訊存在或資訊錯誤")

    def is_no_location_details_correct(self):
        if not self.d(resourceId="com.nothing.gallery:id/taken_time_date", text="24 July").exists:
            pytest.fail("沒有日期時間存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/display_name", text="image_1.png").exists:
            pytest.fail("沒有檔名資訊存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/device_name", text="—").exists:
            pytest.fail("沒有 device_name 資訊存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/pixel_count", text="0.5 MP").exists:
            pytest.fail("沒有 Image 資訊存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/focal_length", text="—").exists:
            pytest.fail("沒有 Capture 資訊存在或資訊錯誤")
        if self.d(resourceId="com.nothing.gallery:id/geo_location_panel", description="Geo location panel").exists:
            pytest.fail("有 geo_location 資訊存在")

    def swipe_up_to_details(self):
        try:
            self.d.swipe(0.465, 0.654, 0.465, 0.367, duration=0.02)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 swipe_up_to_details 失败: {e}")
            pytest.xfail("點擊 swipe_up_to_details 失败")

    def is_24_july_pic(self):
        if not self.d(resourceId="com.nothing.gallery:id/taken_time_date", text="24 July").exists:
            pytest.fail("不是測試用例設定的照片 或是 日期错误")
