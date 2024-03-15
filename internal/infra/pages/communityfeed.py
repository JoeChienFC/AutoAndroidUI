import uiautomator2 as u2
import time,pytest


class CommunityFeed:

    def __init__(self):
        self.d = u2.connect()
        self.btn_locationpicker_x_y = (0.417, 0.063)
        self.icon_menu_x_y = (0.929, 0.06)
        self.icon_create_x_y = (0.891, 0.836)
        self.text_community_name_x_y = (0.173, 0.113)
        self.pic_headshot_x_y = (0.091, 0.153)
        self.text_username_x_y = (0.22, 0.151)
        self.text_location_x_y = ()
        self.comment_text_x_y = (0.076, 0.287)
        self.comment_media_x_y = (0.523, 0.266)
        self.icon_comment_xpath = '//android.widget.ScrollView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]'
        self.icon_share_xpath = '//android.widget.ScrollView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[3]'
        self.icon_like_xpath = '//android.widget.ScrollView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[4]'
        self.icon_more_xpath = '//android.widget.ScrollView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[5]'

    def btn_locationpicker_click(self):
        try:
            # 點擊 location picker
            self.d.click(*self.btn_locationpicker_x_y)
            time.sleep(2)
            from internal.infra.pages.community_location_picker import CommunityLocationPicker
            return CommunityLocationPicker()

        except Exception as e:
            print(f"點 locationpicker 失败: {e}")
            pytest.xfail("點 locationpicker 失败")

    def icon_menu_click(self):
        try:
            self.d.click(*self.icon_menu_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_menu 失败: {e}")
            pytest.xfail("點 icon_menu 失败")

    def icon_create_click(self):
        try:
            self.d.click(*self.icon_create_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_create 失败: {e}")
            pytest.xfail("點 icon_create 失败")

    def text_communityname_click(self):
        try:
            self.d.click(*self.text_community_name_x_y)
            time.sleep(1)

            from internal.infra.pages.community_page import CommunityPage
            return CommunityPage()

        except Exception as e:
            print(f"點 text_community_name 失败: {e}")
            pytest.xfail("點 text_community_name 失败")

    def pic_headshot_click(self):
        try:
            self.d.click(*self.pic_headshot_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 pic_headshot 失败: {e}")
            pytest.xfail("點 pic_headshot 失败")

    def text_username_click(self):
        try:
            self.d.click(*self.text_username_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 text_username 失败: {e}")
            pytest.xfail("點 text_username 失败")

    def comment_text_click(self):
        try:
            self.d.click(*self.comment_text_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 comment_text 失败: {e}")
            pytest.xfail("點 comment_text 失败")

    def comment_media_click(self):
        try:
            self.d.click(*self.comment_media_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 comment_media 失败: {e}")
            pytest.xfail("點 comment_media 失败")

    def icon_comment_click(self):
        try:
            self.d.xpath(self.icon_comment_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_comment 失败: {e}")
            pytest.xfail("點 icon_comment 失败")

    def icon_share_click(self):
        try:
            self.d.xpath(self.icon_share_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_share 失败: {e}")
            pytest.xfail("點 icon_share 失败")

    def icon_like_click(self):
        try:
            self.d.xpath(self.icon_like_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_like 失败: {e}")
            pytest.xfail("點 icon_like 失败")

    def icon_more_click(self):
        try:
            self.d.xpath(self.icon_more_xpath).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_more 失败: {e}")
            pytest.xfail("點 icon_more 失败")

    def screen_swipeupanddown(self):
        try:
            time.sleep(1)
            self.d.swipe_ext("up")

        except Exception as e:
            print(f"上滑 screen 失败: {e}")
            pytest.xfail("上滑 screen 失败")

    def myprofile_click(self):
        try:
            if self.d(description="Tab 5 of 5").exists(7):
                self.d(description="Tab 5 of 5").click()
                print("成功進入 myprofile！")
                time.sleep(2)
                from internal.infra.pages.myprofile import MyProfile
                return MyProfile()
            else:
                pytest.xfail("進入 myprofile 失败")
        except Exception as e:
            print(f"進入 myprofile 失败: {e}")
            pytest.xfail("進入 myprofile 失败")

    def explore_click(self):
        try:
            if self.d(description="Tab 4 of 5").exists(5):
                self.d(description="Tab 4 of 5").click()
                print("成功進入 explore！")
                from internal.infra.pages.explore import Explore
                return Explore()

        except Exception as e:
            print(f"進入 explore 失败: {e}")
            pytest.xfail("進入 explore 失败")

    def ai_click(self):
        try:
            if self.d(description="Tab 3 of 5").exists(5):
                self.d(description="Tab 3 of 5").click()
                print("成功進入ai！")
                time.sleep(2)
                from internal.infra.pages.spotfeed import SpotFeed
                return SpotFeed()
        except Exception as e:
            print(f"進入 ai 失败: {e}")
            pytest.xfail("進入 ai 失败")

    def spot_click(self):
        try:
            if self.d(description="Tab 2 of 5").exists(5):
                self.d(description="Tab 2 of 5").click()
                print("成功進入spot！")
                time.sleep(2)
                from internal.infra.pages.spotfeed import SpotFeed
                return SpotFeed()
        except Exception as e:
            print(f"進入spot失败: {e}")
            pytest.xfail("進入spot失败")

    def community_click(self):
        try:
            if self.d(description="Tab 1 of 5").exists(5):
                self.d(description="Tab 1 of 5").click()
                print("成功進入community！")
                time.sleep(2)
                from internal.infra.pages.spotfeed import SpotFeed
                return SpotFeed()
        except Exception as e:
            print(f"進入 community 失败: {e}")
            pytest.xfail("進入 community 失败")

