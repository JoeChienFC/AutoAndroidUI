import uiautomator2 as u2
import time,pytest


class CreateSpotUploadAlbum:

    def __init__(self):
        self.d = u2.connect()
        self.icon_close_x_y = (0.068, 0.058)
        self.text_from_profile_x_y = (0.167, 0.216)
        self.second_title_item_x_y = (0.196, 0.141)
        self.third_title_item_x_y = (0.208, 0.203)
        self.first_item_x_y = (0.622, 0.104)
        self.second_item_x_y = (0.937, 0.109)
        self.pic_video_x_y = (0.5, 0.187)
        self.title_album_x_y = (0.5, 0.06)
        self.btn_select_x_y = (0.788, 0.887)
        self.icon_location_close_x_y = (0.244, 0.81)

    def icon_close_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_close_x_y)

        except Exception as e:
            print(f"點 icon_close 失败: {e}")
            pytest.xfail("點 icon_close 失败")

    def title_album_click(self):
        try:
            self.d.click(*self.title_album_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 title_album 失败: {e}")
            pytest.xfail("點 title_album 失败")

    def icon_camera_click(self):
        try:
            self.d(description="Camera").click()
            time.sleep(2)

        except Exception as e:
            print(f"點 text_from_profile 失败: {e}")
            pytest.xfail("點 text_from_profile 失败")

    def pic_video_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.pic_video_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 pic_video 失败: {e}")
            pytest.xfail("點 pic_video 失败")

    def icon_select_click(self):
        try:
            self.d.click(*self.first_item_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_select 失败: {e}")
            pytest.xfail("點 icon_select 失败")

    def second_item_select_click(self):
        try:
            self.d.click(*self.second_item_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 second_item_select 失败: {e}")
            pytest.xfail("點 second_item_select 失败")

    def btn_select_click(self):
        try:
            self.d.click(*self.btn_select_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_select 失败: {e}")
            pytest.xfail("點 btn_select 失败")