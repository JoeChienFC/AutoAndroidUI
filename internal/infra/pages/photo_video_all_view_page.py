import uiautomator2 as u2
import time, pytest
import os


class PhotoVideoAllViewPage:

    def __init__(self):
        self.thumbnail = "Thumbnail"
        self.share_icon = "Share"
        self.more_icon = "More options"
        self.delete_icon = "Delete"
        self.photo = "Thumbnail"
        self.btn_more_options = "More options"
        self.favorite = "Favourite"
        self.un_favorite = "Unfavourite"

        self.d = u2.connect()

    def icon_favorite_click(self):
        try:
            if self.d(description=self.favorite).exists:
                self.d(description=self.favorite).click()
                time.sleep(1)

        except Exception as e:
            print(f"點擊 icon_favorite 失败: {e}")
            pytest.xfail("點擊 icon_favorite 失败")

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

            from internal.infra.pages.delete_media_popup import DeleteMediaPopup
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
        if not self.d(resourceId="com.nothing.gallery:id/taken_time_date", text="9 August 2024").exists:
            pytest.fail("沒有日期時間存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/display_name", text="location_pic.jpg").exists:
            pytest.fail("沒有檔名資訊存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/device_name", text="NOTHING A065").exists:
            pytest.fail("沒有 device_name 資訊存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/pixel_count", text="12.6 MP").exists:
            pytest.fail("沒有 Image 資訊存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/focal_length", text="5.59 MM").exists:
            pytest.fail("沒有 Capture 資訊存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/geo_location_panel", description="Geo location panel").exists:
            pytest.fail("沒有 geo_location 資訊存在或資訊錯誤")

    def is_no_location_details_correct(self):
        if not self.d(resourceId="com.nothing.gallery:id/taken_time_date", text="9 August 2024").exists:
            pytest.fail("沒有日期時間存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/display_name", text="image_3.png").exists:
            pytest.fail("沒有檔名資訊存在或資訊錯誤")
        if not self.d(resourceId="com.nothing.gallery:id/pixel_count", text="0.5 MP").exists:
            pytest.fail("沒有 Image 資訊存在或資訊錯誤")
        if self.d(resourceId="com.nothing.gallery:id/geo_location_panel", description="Geo location panel").exists:
            pytest.fail("有 geo_location 資訊存在")

    def swipe_up_to_details(self):
        try:
            time.sleep(1)
            self.d.swipe(0.465, 0.654, 0.465, 0.367, duration=0.03)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 swipe_up_to_details 失败: {e}")
            pytest.xfail("點擊 swipe_up_to_details 失败")

    def is_july_24_pic(self):
        if not self.d(resourceId="com.nothing.gallery:id/taken_time_date", text="24 July 2024").exists:
            pytest.fail("不是測試用例設定的照片 或是 日期错误")

    def is_burst_amount(self, photos=str):
        if not self.d(resourceId="com.nothing.gallery:id/count", text=photos).exists:
            pytest.fail(f"堆疊的照片數量錯誤{photos} 或是 沒有堆疊顯示")

    def check_filmstrip_items(self, photos=int):
        elements = self.d(resourceId="com.nothing.gallery:id/filmstrip_thumb_bar_item")
        if elements.count != photos:
            pytest.fail(f"堆疊照片展開後的照片數量錯誤{photos}")

    def check_crown_icon(self):
        if not self.d(resourceId="com.nothing.gallery:id/icon").exists:
            pytest.fail("堆疊照片展開後顯示堆疊照片封面的皇冠圖標沒有出現")

    def swipe_down_to_exit(self):
        try:
            time.sleep(1)
            self.d.swipe(0.465, 0.367, 0.465, 0.654, duration=0.03)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 swipe_down_to_exit 失败: {e}")
            pytest.xfail("點擊 swipe_down_to_exit 失败")

    def swipe_left_to_next(self):
        try:
            time.sleep(1)
            self.d.swipe(0.754, 0.465, 0.267, 0.465, duration=0.03)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 swipe_left_to_next 失败: {e}")
            pytest.xfail("點擊 swipe_left_to_next 失败")

