import uiautomator2 as u2
import time


class SpotLocationPicker:

    def __init__(self):
        self.d = u2.connect()

        self.like_icon_xpath = '//android.widget.Button'

        self.community_name = (0.489, 0.061)
        self.create_icon_x_y = (0.91, 0.059)
        self.back_icon_x_y = (0.058, 0.061)
        self.comment_icon_x_y = (0.928, 0.725)
        self.share_icon_x_y = (0.934, 0.792)
        self.more_icon_x_y = (0.924, 0.855)
        self.headshot_pic_x_y = (0.089, 0.74)
        self.username_text_x_y = (0.174, 0.743)
        self.location_icon_x_y = (0.061, 0.857)
        self.screen_mute_x_y = (0.503, 0.425)
        self.text_sharecommunity_x_y = (0.113, 0.823)
        self.text_caption_x_y = (0.061, 0.788)

    def bar_search_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.back_icon_x_y)

        except Exception as e:
            print(f"點擊 back_icon 失败: {e}")
            assert False, "點擊 back_icon 失败"