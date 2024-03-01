import uiautomator2 as u2
import time


class Comment:

    def __init__(self):
        self.d = u2.connect()

        self.comment_video_x_y = (0.493, 0.357)

    def comment_video_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.comment_video_x_y)

        except Exception as e:
            print(f"點擊 comment_video 失败: {e}")
            assert False, "點擊 comment_video 失败"

