import uiautomator2 as u2
import time


class HomeFeed:

    def __init__(self):
        self.d = u2.connect()
        self.location_picker_xpath = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]'
        self.add_icon_xpath = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]'
        self.like_icon_xpath = '//android.widget.Button'
        self.icon_create_xpath = '//android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]'
        self.comment_icon_x_y = (0.928, 0.725)
        self.share_icon_x_y = (0.934, 0.792)
        self.more_icon_x_y = (0.924, 0.855)
        self.headshot_pic_x_y = (0.089, 0.788)
        self.username_text_x_y = (0.184, 0.775)
        self.location_icon_x_y = (0.061, 0.857)
        self.screen_mute_x_y = (0.503, 0.425)
        self.text_sharecommunity_x_y = (0.113, 0.823)
        self.text_caption_x_y = (0.061, 0.821)

        self.home_feed_setup()

    def home_feed_setup(self):
        try:
            if self.d(description="縮小").exists(5):
                self.d(description="縮小").click()
        except Exception as e:
            print(f"An error occurred during setup: {e}")

    def icon_create_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.icon_create_xpath).click()

        except Exception as e:
            print(f"點擊 icon_create 失败: {e}")
            assert False, "點擊 icon_create 失败"

    def text_caption_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_caption_x_y)

        except Exception as e:
            print(f"點擊 text_caption 失败: {e}")
            assert False, "點擊 text_caption 失败"

    def text_sharecommunity_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_sharecommunity_x_y)

        except Exception as e:
            print(f"點擊 text_sharecommunity 失败: {e}")
            assert False, "點擊 text_sharecommunity 失败"

    def screen_swipeupanddown(self):
        try:
            time.sleep(1)
            self.d.swipe_ext("up")

        except Exception as e:
            print(f"上滑 screen 失败: {e}")
            assert False, "上滑 screen 失败"

    def screen_swipeleft(self):
        try:
            time.sleep(1)
            self.d.swipe_ext("left")
            print("成功左滑！")

        except Exception as e:
            print(f"左滑 screen 失败: {e}")
            assert False, "左滑 screen 失败"

    def screen_longclick(self):
        try:
            time.sleep(1)
            self.d.long_click(*self.screen_mute_x_y)

        except Exception as e:
            print(f"長按 screen 失败: {e}")
            assert False, "長按 screen 失败"

    def screen_doubleclick(self):
        try:
            time.sleep(1)
            self.d.double_click(*self.screen_mute_x_y)

        except Exception as e:
            print(f"雙擊 screen 失败: {e}")
            assert False, "雙擊 screen 失败"

    def screen_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.screen_mute_x_y)

        except Exception as e:
            print(f"點擊 screen 失败: {e}")
            assert False, "點擊 screen 失败"

    def text_location_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.location_icon_x_y)

        except Exception as e:
            print(f"點擊 location_icon 失败: {e}")
            assert False, "點擊 location_icon 失败"

    def text_username_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.username_text_x_y)

        except Exception as e:
            print(f"點擊 username_text 失败: {e}")
            assert False, "點擊 username_text 失败"

    def pic_headshot_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.headshot_pic_x_y)

        except Exception as e:
            print(f"點擊 headshot_pic 失败: {e}")
            assert False, "點擊 headshot_pic 失败"

    def icon_more_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.more_icon_x_y)

        except Exception as e:
            print(f"點擊 more 失败: {e}")
            assert False, "點擊 more 失败"

    def icon_share_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.share_icon_x_y)
            time.sleep(1)
            from internal.infra.pages.shareto_popup import ShareToPopup
            return ShareToPopup()

        except Exception as e:
            print(f"點擊 share 失败: {e}")
            assert False, "點擊 share 失败"

    def icon_comment_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.comment_icon_x_y)

        except Exception as e:
            print(f"點擊 comment 失败: {e}")
            assert False, "點擊 comment 失败"

    def icon_like_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.like_icon_xpath).click()

        except Exception as e:
            print(f"點擊 like 失败: {e}")
            assert False, "點擊 like 失败"

    def btn_follow_click(self):
        try:
            if self.d(description="F​o​l​l​o​w").exists(2):
                self.d(description="F​o​l​l​o​w").click()
            else:
                assert False, "沒有找到 follow 按鈕"

        except Exception as e:
            print(f"點擊 follow 失败: {e}")
            assert False, "點擊 follow 失败"

    def location_picker_click(self):
        try:
            # 點擊 location picker
            self.d.xpath(self.location_picker_xpath).click()
            time.sleep(2)
            from internal.infra.pages.spot_location_picker import SpotLocationPicker
            return SpotLocationPicker()

        except Exception as e:
            print(f"進入 location_picker 失败: {e}")
            assert False, "進入 location_picker 失败"

    def icon_create_click(self):
        try:
            # 點擊 location picker
            self.d.xpath(self.add_icon_xpath).click()
            time.sleep(2)

        except Exception as e:
            print(f"進入 add_icon 失败: {e}")
            assert False, "進入 add_icon 失败"

    def btn_unfollow_click(self):
        try:
            if self.d(description="F​o​l​l​o​w​i​n​g").exists(2):
                self.d(description="F​o​l​l​o​w​i​n​g").click()
            else:
                assert False, "沒有找到 following 按鈕"

        except Exception as e:
            print(f"點擊 following 失败: {e}")
            assert False, "點擊 following 失败"

    '''
    -------------------------------------------
    '''

    def enter_community(self):

        try:
            if self.d(description="Tab 2 of 5").exists(5):
                self.d(description="Tab 2 of 5").click()
                print("成功進入community！")
                time.sleep(10)

                from internal.infra.pages.communityfeed import CommunityFeed
                return CommunityFeed()
        except Exception as e:
            print(f"進入community失败: {e}")
            assert False, "進入community失败"

    def enter_ailex_page(self):

        try:
            if self.d(description="Tab 3 of 5").exists(5):
                self.d(description="Tab 3 of 5").click()
                print("成功進入Ailex page！")
                time.sleep(10)
                # return CommunityFeed()
        except Exception as e:
            print(f"進入Ailex page失败: {e}")
            assert False, "進入Ailex page失败"

    def enter_search_page(self):

        try:
            if self.d(description="Tab 4 of 5").exists(5):
                self.d(description="Tab 4 of 5").click()
                print("成功進入Search page！")
                time.sleep(10)
                # return CommunityFeed()
        except Exception as e:
            print(f"進入Search page失败: {e}")
            assert False, "進入Search page失败"

    def enter_my_profile_page(self):

        try:
            if self.d(description="Tab 5 of 5").exists(5):
                self.d(description="Tab 5 of 5").click()
                print("成功進入My Profile page！")
                time.sleep(5)
                # return CommunityFeed()
        except Exception as e:
            print(f"進入My Profile page失败: {e}")
            assert False, "進入My Profile page失败"

    def swipe_up_next_post(self):

        try:
            self.d.swipe_ext("up")
            print("成功上滑！")
            time.sleep(1)
            # return CommunityFeed()
        except Exception as e:
            print(f"上滑失败: {e}")
            assert False, "上滑失败"

    def swipe_down_previous_post(self):

        try:
            self.d.swipe_ext("down")
            print("成功下滑！")
            time.sleep(1)
            # return CommunityFeed()
        except Exception as e:
            print(f"下滑失败: {e}")
            assert False, "下滑失败"
