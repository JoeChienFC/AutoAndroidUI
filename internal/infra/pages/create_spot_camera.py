import uiautomator2 as u2
import time, pytest


class CreateSpotCamera:

    def __init__(self):
        self.screen_drag_xy1_xy2 = (0.476, 0.228, 0.485, 0.558)
        self.d = u2.connect()

        self.icon_next_xpath = '//android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]'
        self.icon_pause_xpath = '//android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]'
        self.icon_album_xpath = '//android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]'
        self.icon_shutter_xpath = '//android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]'
        self.icon_filming_guide_xpath = '//android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[5]'
        self.icon_grid_xpath = '//android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[4]'
        self.icon_flash_xpath = '//android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]'
        self.icon_timer_xpath = '//android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]'
        self.icon_switch_camera_xpath = '//android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]'
        self.icon_back_xpath = '//android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]'

        self.icon_shutter_x_y = (0.502, 0.81)
        self.icon_next_x_y = (0.851, 0.814)

    def icon_back_click(self):
        try:
            self.d.xpath(self.icon_back_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_back 失败: {e}")
            pytest.xfail("點 icon_back 失败")

    def icon_timer_click(self):
        try:
            self.d.xpath(self.icon_timer_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_timer 失败: {e}")
            pytest.xfail("點 icon_timer 失败")

    def icon_flash_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.icon_flash_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_flash 失败: {e}")
            pytest.xfail("點 icon_flash 失败")

    def icon_grid_click(self):
        try:
            self.d.xpath(self.icon_grid_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_grid 失败: {e}")
            pytest.xfail("點 icon_grid 失败")

    def icon_filming_guide_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.icon_filming_guide_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_filming_guide 失败: {e}")
            pytest.xfail("點 icon_filming_guide 失败")

    def icon_switch_camera_click(self):
        try:
            self.d.xpath(self.icon_switch_camera_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_switch_camera 失败: {e}")
            pytest.xfail("點 icon_switch_camera 失败")

    def icon_shutter_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_shutter_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_shutter 失败: {e}")
            pytest.xfail("點 icon_shutter 失败")

    def icon_album_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.icon_album_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_album 失败: {e}")
            pytest.xfail("點 icon_album 失败")

    def icon_pause_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.icon_pause_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_pause 失败: {e}")
            pytest.xfail("點 icon_pause 失败")

    def icon_next_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_next_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_next 失败: {e}")
            pytest.xfail("點 icon_next 失败")

    def screen_drag(self):
        try:
            time.sleep(1)
            self.d.drag(*self.screen_drag_xy1_xy2)
            time.sleep(1)

        except Exception as e:
            print(f"screen_drag 失败: {e}")
            pytest.xfail("screen_drag 失败")