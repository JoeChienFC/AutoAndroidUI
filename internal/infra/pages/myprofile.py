import uiautomator2 as u2
import time


class MyProfile:

    def __init__(self):
        self.d = u2.connect()
        self.activities_page_x_y = (0.756, 0.356)

        self.comment_x_y = (0.551, 0.439)
        self.first_video_x_y = (0.16, 0.505)

    def first_video_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.first_video_x_y)
            from internal.infra.pages.spot_page import SpotPage
            return SpotPage()

        except Exception as e:
            print(f"點擊 first_video 失败: {e}")
            assert False, "點擊 first_video 失败"

    def activities_click(self):
        try:
            self.d.click(*self.activities_page_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 activities_page 失败: {e}")
            assert False, "點擊 activities_page 失败"

    def comment_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.comment_x_y)

            from internal.infra.pages.comment import Comment
            return Comment()

        except Exception as e:
            print(f"點擊 comment_video 失败: {e}")
            assert False, "點擊 comment_video 失败"
