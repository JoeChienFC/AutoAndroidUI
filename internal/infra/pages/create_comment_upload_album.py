import uiautomator2 as u2
import time


class CreateCommentUploadAlbum:

    def __init__(self):
        self.d = u2.connect()
        self.text_from_profile_x_y = (0.167, 0.216)

    def text_from_profile_click(self):
        try:
            self.d.click(*self.text_from_profile_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 text_from_profile 失败: {e}")
            assert False, "點 text_from_profile 失败"

