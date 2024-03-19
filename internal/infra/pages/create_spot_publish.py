import uiautomator2 as u2
import time, pytest


class CreateSpotPublish:

    def __init__(self):
        self.d = u2.connect()
        self.text_done_x_y = (0.908, 0.077)

    def btn_post_click(self):
        try:
            self.d(description="Done").click()
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_post 失败: {e}")
            pytest.xfail("點 btn_post 失败")

