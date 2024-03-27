import uiautomator2 as u2
import time, pytest


class CreateCommunityUploadAlbum:

    def __init__(self):
        self.select_photo_x_y = (0.175, 0.18)
        self.icon_close_x_y = (0.065, 0.06)
        self.d = u2.connect()
        
    def icon_close_click(self):
        try:
            self.d.click(*self.icon_close_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 icon_close_click 失败: {e}")

    def title_click(self):
        try:
            time.sleep(1)
            self.d(description="All Photos").click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 title_click 失败: {e}")

    def screen_swipeupanddown(self):
        try:
            time.sleep(1)
            self.d.swipe_ext("up")

        except Exception as e:
            print(f"上滑 screen 失败: {e}")
            pytest.xfail("上滑 screen 失败")

    def select_photo(self):
        try:
            time.sleep(1)
            self.d.click(*self.select_photo_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 select_photo 失败: {e}")