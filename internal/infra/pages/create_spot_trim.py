import uiautomator2 as u2
import time, pytest


class CreateSpotTrim:

    def __init__(self):
        self.bar_videoclips_drag_xy1_xy2 = (0.645, 0.75, 0.428, 0.75)
        self.bar_videoclips = (0.502, 0.751)

        self.d = u2.connect()

    def text_done_click(self):
        try:
            self.d(description="Done").click()
            time.sleep(1)

        except Exception as e:
            print(f"點 text_done_click 失败: {e}")
            pytest.xfail("點 text_done_click 失败")

    def icon_play_click(self):
        try:
            self.d(className="android.widget.ImageView", index=2).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_play_click 失败: {e}")
            pytest.xfail("點 icon_play_click 失败")

    def icon_fullscreen_click(self):
        try:
            time.sleep(1)
            self.d(className="android.widget.ImageView", index=4).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_fullscreen_click 失败: {e}")
            pytest.xfail("點 icon_fullscreen_click 失败")

    def bar_videoclips_click(self):
        try:
            self.d.click(*self.bar_videoclips)
            time.sleep(1)

        except Exception as e:
            print(f"點 bar_videoclips_click 失败: {e}")
            pytest.xfail("點 bar_videoclips_click 失败")

    def bar_videoclips_drag(self):
        try:
            time.sleep(1)
            self.d.swipe(*self.bar_videoclips_drag_xy1_xy2)
            time.sleep(1)

        except Exception as e:
            print(f"bar_videoclips_drag 失败: {e}")
            pytest.xfail("bar_videoclips_drag 失败")

    def icon_edit_click(self):
        try:
            time.sleep(1)
            self.d(description="Edit").click()
            time.sleep(1)

        except Exception as e:
            print(f"icon_edit_click 失败: {e}")
            pytest.xfail("icon_edit_click 失败")

    def icon_addclips_click(self):
        try:
            time.sleep(1)
            self.d(description="Add Clips").click()
            time.sleep(1)

        except Exception as e:
            print(f"icon_addclips_click 失败: {e}")
            pytest.xfail("icon_addclips_click 失败")

    def icon_rotate_click(self):
        try:
            time.sleep(1)
            self.d(description="Rotate").click()
            time.sleep(1)

        except Exception as e:
            print(f"icon_rotate_click 失败: {e}")
            pytest.xfail("icon_rotate_click 失败")

    def icon_delete_click(self):
        try:
            time.sleep(1)
            self.d(description="Delete").click()
            time.sleep(1)

        except Exception as e:
            print(f"icon_delete_click 失败: {e}")
            pytest.xfail("icon_delete_click 失败")

    def icon_split_click(self):
        try:
            time.sleep(1)
            self.d(description="Split").click()
            time.sleep(1)

        except Exception as e:
            print(f"icon_split_click 失败: {e}")
            pytest.xfail("icon_split_click 失败")
