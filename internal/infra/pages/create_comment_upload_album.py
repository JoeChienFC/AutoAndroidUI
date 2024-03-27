import uiautomator2 as u2
import time,pytest


class CreateCommentUploadAlbum:

    def __init__(self):
        self.icon_close_x_y = (0.059, 0.06)
        self.d = u2.connect()
        self.first_video_from_profile_x_y = (0.167, 0.216)
        self.second_title_item_x_y = (0.196, 0.141)
        self.third_title_item_x_y = (0.208, 0.203)
        self.first_item_x_y = (0.619, 0.434)
        self.second_item_x_y = (0.839, 0.487)
        self.third_item_x_y = (0.166, 0.627)
        self.fourth_item_x_y = (0.494, 0.635)
        self.fifth_item_x_y = (0.833, 0.633)
        self.title_album_x_y = (0.5, 0.06)
        self.btn_select_x_y = (0.788, 0.887)
        self.icon_location_close_x_y = (0.244, 0.81)

    def icon_close_click(self):
        try:
            self.d.click(*self.icon_close_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_close_click 失败: {e}")
            pytest.xfail("點 icon_close_click 失败")

    def icon_camera_click(self):
        try:
            self.d(description="Camera").click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_camera_click 失败: {e}")
            pytest.xfail("點 icon_camera_click 失败")

    def change_pic_album(self):
        try:
            time.sleep(1)
            self.title_album_click()
            time.sleep(1)
            self.d.click(*self.third_title_item_x_y)

        except Exception as e:
            print(f"點 change_pic_album 失败: {e}")
            pytest.xfail("點 change_pic_album 失败")

    def change_video_album(self):
        try:
            time.sleep(1)
            self.title_album_click()
            time.sleep(1)
            self.d.click(*self.second_title_item_x_y)

        except Exception as e:
            print(f"點 change_video_album 失败: {e}")
            pytest.xfail("點 change_video_album 失败")

    def select_5_pic_or_video(self):
        try:
            time.sleep(1)
            self.d.click(*self.first_item_x_y)
            time.sleep(0.3)
            self.d.click(*self.second_item_x_y)
            time.sleep(0.3)
            self.d.click(*self.third_item_x_y)
            time.sleep(0.3)
            self.d.click(*self.fourth_item_x_y)
            time.sleep(0.3)
            self.d.click(*self.fifth_item_x_y)
            time.sleep(0.3)

        except Exception as e:
            print(f"點 change_album 失败: {e}")
            pytest.xfail("點 change_album 失败")

    def title_album_click(self):
        try:
            self.d.click(*self.title_album_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 title_album 失败: {e}")
            pytest.xfail("點 title_album 失败")

    def select_video_from_profile_click(self):
        try:
            self.d.click(*self.first_video_from_profile_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 select_video_from_profile_click 失败: {e}")
            pytest.xfail("點 select_video_from_profile_click 失败")

    def text_from_profile_click(self):
        try:
            self.d(description="Select from profile").click()
            time.sleep(1)

        except Exception as e:
            print(f"點 text_from_profile_click 失败: {e}")
            pytest.xfail("點 text_from_profile_click 失败")

    def pic_profile_video_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.first_video_from_profile_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 pic_profile_video_click 失败: {e}")
            pytest.xfail("點 pic_profile_video_click 失败")

    def first_video_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.first_item_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 first_video_click 失败: {e}")
            pytest.xfail("點 first_video_click 失败")

    def btn_select_click(self):
        try:
            self.d.click(*self.btn_select_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 text_btn_select 失败: {e}")
            pytest.xfail("點 text_btn_select 失败")

    def icon_location_close_click(self):
        try:
            self.d.click(*self.icon_location_close_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_location_close 失败: {e}")
            pytest.xfail("點 icon_location_close 失败")