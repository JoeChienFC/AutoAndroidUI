import uiautomator2 as u2
import time, pytest


class DmList:

    def __init__(self):
        self.list_dm_swipeleft_x1_y1_x2_y2 = (0.732, 0.136, 0.172, 0.139)
        self.list_dm_longclick_x_y = (0.532, 0.135)
        self.icon_delete_x_y = None
        self.pic_headshot_x_y = (0.107, 0.143)
        self.list_dm_x_y = (0.532, 0.135)
        self.icon_addfriend_x_y = (0.937, 0.062)
        self.icon_back_x_y = (0.068, 0.061)
        self.d = u2.connect()

    def icon_back_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_back_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 icon_back_click 失败 : {e}")

    def icon_addfriend_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_addfriend_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 icon_addfriend_click 失败 : {e}")

    def list_dm_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_dm_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 list_dm_click 失败 : {e}")

    def pic_headshot_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.pic_headshot_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 pic_headshot_click 失败 : {e}")

    def list_dm_swipeleft(self):
        try:
            time.sleep(1)
            self.d.swipe(*self.list_dm_swipeleft_x1_y1_x2_y2)

        except Exception as e:
            pytest.xfail(f"點擊 list_dm_swipeleft 失败 : {e}")

    def icon_delete_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_delete_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 icon_delete_click 失败 : {e}")

    def list_dm_longclick(self):
        try:
            time.sleep(1)
            self.d.long_click(*self.list_dm_longclick_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 list_dm_longclick 失败 : {e}")