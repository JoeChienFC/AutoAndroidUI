import uiautomator2 as u2
import time


class CreateCommentLocation:

    def __init__(self):
        self.d = u2.connect()
        self.text_done_x_y = (0.908, 0.077)

    def text_done_click(self):
        try:
            self.d.click(*self.text_done_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 text_done 失败: {e}")
            assert False, "點 text_done 失败"
            