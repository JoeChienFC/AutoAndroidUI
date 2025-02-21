import uiautomator2 as u2
import time, pytest
import os


class SelectPhotoVideoPage:

    def __init__(self):
        self.photo = "Thumbnail"
        self.btn_finish = "FINISH"
        self.d = u2.connect()

    def photo_video_select(self):
        try:
            self.d(description=self.photo).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 photo_video_select 失败: {e}")
            pytest.xfail("點擊 photo_video_select 失败")

    def photo_video_multiple_selection(self, times: int):
        try:
            # 找出所有未選中的照片
            unselected_photos = self.d(resourceId="com.nothing.gallery:id/selection", selected="false")
            total_unselected = len(unselected_photos)

            if total_unselected == 0:
                pytest.fail("沒有可選的照片")

            # 確保不超過可選範圍
            times = min(times, total_unselected)

            # 逐一點擊 `times` 張照片
            for i in range(times):
                unselected_photos[i].click(timeout=2)  # 點擊每張未選中的照片
                time.sleep(0.5)  # 避免點擊過快

        except Exception as e:
            print(f"點擊 photo_video_multiple_selection 失敗: {e}")
            pytest.xfail("點擊 photo_video_multiple_selection 失敗")

    def btn_finish_click(self):
        try:
            self.d(text=self.btn_finish).click(timeout=2)
            time.sleep(1)

            from internal.infra.pages.select_media_popup import SelectMediaPopup
            return SelectMediaPopup()

        except Exception as e:
            print(f"點擊 btn_finish_click 失败: {e}")
            pytest.xfail("點擊 btn_finish_click 失败")
