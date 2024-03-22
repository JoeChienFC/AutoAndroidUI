import uiautomator2 as u2
import time,pytest


class CommunityPage:

    def __init__(self):
        self.d = u2.connect()

        self.like_icon_xpath = '//android.widget.ScrollView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[4]'
        self.comment_more_icon_xpath = '//android.widget.ScrollView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[5]'
        self.share_icon_xpath = '//android.widget.ScrollView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]'
        self.comment_icon_xpath = '//android.widget.ScrollView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]'

        self.back_icon_x_y = (0.067, 0.06)
        self.more_icon_x_y = (0.932, 0.062)
        self.community_name = (0.489, 0.061)
        self.create_icon_x_y = (0.885, 0.833)
        self.text_communitylocation_x_y = (0.058, 0.252)
        self.text_members_x_y = (0.62, 0.254)
        self.share_btn_x_y = (0.914, 0.319)
        self.tab_activities_x_y = (0.235, 0.36)
        self.tab_spots_x_y = (0.75, 0.363)
        self.headshot_pic_x_y = (0.091, 0.43)
        self.username_text_x_y = (0.202, 0.43)
        self.location_icon_x_y = (0.252, 0.483)
        self.comment_text_x_y = (0.982, 0.43)
        self.comment_xpath = '//android.widget.ScrollView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]'
        self.screen_mute_x_y = (0.503, 0.425)
        self.text_sharecommunity_x_y = (0.113, 0.823)
        self.text_caption_x_y = (0.061, 0.788)

    def icon_back_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.back_icon_x_y)

        except Exception as e:
            print(f"點擊 back_icon 失败: {e}")
            pytest.xfail("點擊 back_icon 失败")

    def title_communityname_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.community_name)

        except Exception as e:
            print(f"點擊 icon_create 失败: {e}")
            pytest.xfail("點擊 icon_create 失败")

    def text_communitylocation_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_communitylocation_x_y)

        except Exception as e:
            print(f"點擊 text_communitylocation 失败: {e}")
            pytest.xfail("點擊 text_communitylocation 失败")

    def text_members_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_members_x_y)

        except Exception as e:
            print(f"點擊 text_members 失败: {e}")
            pytest.xfail("點擊 text_members 失败")

    def btn_join_click(self):
        try:
            time.sleep(1)
            if self.d(description="Join").exists:
                self.d(description="Join").click()

        except Exception as e:
            print(f"點擊 btn_join 失败: {e}")
            pytest.xfail("點擊 btn_join 失败")

    def btn_unjoin_click(self):
        try:
            time.sleep(2)
            if self.d(description="Joined").exists:
                self.d(description="Joined").click()

        except Exception as e:
            print(f"點擊 btn_unjoin 失败: {e}")
            pytest.xfail("點擊 btn_unjoin 失败")

    def btn_share_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.share_btn_x_y)

        except Exception as e:
            print(f"點擊 share_btn 失败: {e}")
            pytest.xfail("點擊 share_btn 失败")

    def tab_activities_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.tab_activities_x_y)

        except Exception as e:
            print(f"點擊 tab_activities 失败: {e}")
            pytest.xfail("點擊 tab_activities 失败")

    def tab_spots_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.tab_spots_x_y)

        except Exception as e:
            print(f"點擊 tab_spots 失败: {e}")
            pytest.xfail("點擊 tab_spots 失败")

    def icon_create_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.create_icon_x_y)
            time.sleep(1)

            from internal.infra.pages.create_comment import CreateComment
            return CreateComment()

        except Exception as e:
            print(f"點擊 icon_create 失败: {e}")
            pytest.xfail("點擊 icon_create 失败")

    def screen_swipeupanddown(self):
        try:
            time.sleep(1)
            self.d.swipe_ext("up")

        except Exception as e:
            print(f"上滑 screen 失败: {e}")
            pytest.xfail("上滑 screen 失败")

    def pic_headshot_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.headshot_pic_x_y)

        except Exception as e:
            print(f"點擊 headshot_pic 失败: {e}")
            pytest.xfail("點擊 headshot_pic 失败")

    def text_location_click(self):
        try:
            time.sleep(1.5)
            self.d.click(*self.location_icon_x_y)

        except Exception as e:
            print(f"點擊 location_icon 失败: {e}")
            pytest.xfail("點擊 location_icon 失败")

    def comment_text_click(self):
        try:
            time.sleep(1.5)
            self.d.click(*self.comment_text_x_y)

        except Exception as e:
            print(f"點擊 comment_text 失败: {e}")
            pytest.xfail("點擊 comment_text 失败")

    def comment_click(self):
        try:
            time.sleep(1.5)
            self.d.xpath(self.comment_xpath).click()

        except Exception as e:
            print(f"點擊 comment 失败: {e}")
            pytest.xfail("點擊 comment 失败")

    #-------------------

    def btn_follow_click(self):
        try:
            if self.d(description="F​o​l​l​o​w").exists(2):
                self.d(description="F​o​l​l​o​w").click()
            else:
                pytest.xfail("沒有找到 follow 按鈕")

        except Exception as e:
            print(f"點擊 follow 失败: {e}")
            pytest.xfail("點擊 follow 失败")

    def btn_unfollow_click(self):
        try:
            if self.d(description="F​o​l​l​o​w​i​n​g").exists(2):
                self.d(description="F​o​l​l​o​w​i​n​g").click()
                time.sleep(1)
            else:
                pytest.xfail("沒有找到 following 按鈕")

        except Exception as e:
            print(f"點擊 following 失败: {e}")
            pytest.xfail("點擊 following 失败")

    def icon_like_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.like_icon_xpath).click()

        except Exception as e:
            print(f"點擊 like 失败: {e}")
            pytest.xfail("點擊 like 失败")

    def text_caption_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_caption_x_y)

        except Exception as e:
            print(f"點擊 text_caption 失败: {e}")
            pytest.xfail("點擊 text_caption 失败")

    def text_sharecommunity_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_sharecommunity_x_y)

        except Exception as e:
            print(f"點擊 text_sharecommunity 失败: {e}")
            pytest.xfail("點擊 text_sharecommunity 失败")


    def screen_swipeleft(self):
        try:
            time.sleep(1)
            self.d.swipe_ext("left")
            print("成功左滑！")

        except Exception as e:
            print(f"左滑 screen 失败: {e}")
            pytest.xfail("左滑 screen 失败")

    def screen_longclick(self):
        try:
            time.sleep(1)
            self.d.long_click(*self.screen_mute_x_y)

        except Exception as e:
            print(f"長按 screen 失败: {e}")
            pytest.xfail("長按 screen 失败")

    def screen_doubleclick(self):
        try:
            time.sleep(1)
            self.d.double_click(*self.screen_mute_x_y)

        except Exception as e:
            print(f"雙擊 screen 失败: {e}")
            pytest.xfail("雙擊 screen 失败")

    def screen_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.screen_mute_x_y)

        except Exception as e:
            print(f"點擊 screen 失败: {e}")
            pytest.xfail("點擊 screen 失败")

    def text_username_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.username_text_x_y)

        except Exception as e:
            print(f"點擊 username_text 失败: {e}")
            pytest.xfail("點擊 username_text 失败")

    def icon_more_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.more_icon_x_y)

        except Exception as e:
            print(f"點擊 右上角more 失败: {e}")
            pytest.xfail("點擊 右上角more 失败")

    def comment_icon_more_click(self):
        try:
            time.sleep(7)
            self.d.xpath(self.comment_more_icon_xpath).click()

            from internal.infra.pages.comment_more_popup import CommentMorePopup
            return CommentMorePopup()

        except Exception as e:
            print(f"點擊 more 失败: {e}")
            pytest.xfail("點擊 more 失败")

    def icon_share_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.share_icon_xpath).click()
            time.sleep(1)
            from internal.infra.pages.shareto_popup import ShareToPopup
            return ShareToPopup()

        except Exception as e:
            print(f"點擊 share 失败: {e}")
            pytest.xfail("點擊 share 失败")

    def icon_comment_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.comment_icon_xpath).click()

        except Exception as e:
            print(f"點擊 comment 失败: {e}")
            pytest.xfail("點擊 comment 失败")

