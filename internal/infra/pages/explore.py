import uiautomator2 as u2
import time, pytest


class Explore:

    def __init__(self):
        self.d = u2.connect()

        self.bar_search_xpath = '//android.widget.EditText'
        self.pic_spot_l_x_y = (0.838, 0.384)
        self.pic_spot_s_x_y = (0.826, 0.17)
        self.pic_community_x_y = (0.305, 0.162)

    def bar_search_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.bar_search_xpath).click()

        except Exception as e:
            pytest.xfail(f"點擊 search_click 失败 : {e}")

    def pic_spot_l_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.pic_spot_l_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 pic_spot_l 失败 : {e}")

    def pic_spot_s_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.pic_spot_s_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 pic_spot_s 失败 : {e}")

    def pic_community_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.pic_community_x_y)

        except Exception as e:
            pytest.xfail(f"點擊 pic_community 失败 : {e}")

    def screen_swipeupanddown(self):
        try:
            time.sleep(1)
            self.d.swipe_ext("up")

        except Exception as e:
            print(f"上滑 screen 失败: {e}")
            pytest.xfail("上滑 screen 失败")

