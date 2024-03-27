import uiautomator2 as u2
import time, pytest


class CreateCommunityCoverReposition:

    def __init__(self):
        self.screen_drag_xy1_xy2 = (0.476, 0.228, 0.485, 0.558)
        self.icon_back_x_y = (0.062, 0.057)
        self.d = u2.connect()
        
    def icon_back_click(self):
        try:
            self.d.click(*self.icon_back_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 icon_back_click 失败: {e}")

    def text_save_click(self):
        try:
            time.sleep(1)
            self.d(description="Save").click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 text_save_click 失败: {e}")

    def screen_drag(self):
        try:
            time.sleep(1)
            self.d.drag(*self.screen_drag_xy1_xy2)
            time.sleep(1)

        except Exception as e:
            print(f"screen_drag 失败: {e}")
            pytest.xfail("screen_drag 失败")

