import uiautomator2 as u2
import time,pytest


class CommunityFeed:

    def __init__(self):
        self.d = u2.connect()
        self.btn_locationpicker = "btn_locationpicker"
        self.icon_menu = "icon_menu"
        self.icon_create_x_y = (0.891, 0.836)
        self.text_community_name = "text_communityname"
        self.pic_headshot = "pic_headshot"
        self.text_username = "text_username"
        self.text_location_x_y = ()
        self.comment_text = "comment_text"
        self.comment_media = "comment_media"
        self.icon_comment = "icon_comment"
        self.icon_share = "icon_share"
        self.icon_like = "icon_like"
        self.icon_unlike = "icon_unlike"
        self.icon_more = "icon_more"
        self.icon_unsave = "icon_unsave"
        self.icon_save = "icon_save"

    def btn_locationpicker_click(self):
        try:
            # 點擊 location picker
            self.d(description=self.btn_locationpicker).click(timeout=2)
            # time.sleep(2)
            from internal.infra.pages.community_location_picker import CommunityLocationPicker
            return CommunityLocationPicker()

        except Exception as e:
            print(f"點 locationpicker 失败: {e}")
            pytest.xfail("點 locationpicker 失败")

    def icon_menu_click(self):
        try:
            self.d(description=self.icon_menu).click()
            time.sleep(1)

            from internal.infra.pages.community_feed_dropdown_menu import CommunityFeedDropdownMenu
            return CommunityFeedDropdownMenu()

        except Exception as e:
            print(f"點 icon_menu 失败: {e}")
            pytest.xfail("點 icon_menu 失败")

    # def icon_create_click(self):
    #     try:
    #         self.d.click(*self.icon_create_x_y)
    #         time.sleep(1)
    #
    #         from internal.infra.pages.create_comment import CreateComment
    #         return CreateComment()
    #
    #     except Exception as e:
    #         print(f"點 icon_create 失败: {e}")
    #         pytest.xfail("點 icon_create 失败")

    def text_communityname_click(self):
        try:
            self.d(description=self.text_community_name).click()
            time.sleep(2)

            from internal.infra.pages.community_page import CommunityPage
            return CommunityPage()

        except Exception as e:
            print(f"點 text_community_name 失败: {e}")
            pytest.xfail("點 text_community_name 失败")

    def pic_headshot_click(self):
        try:
            self.d(description=self.pic_headshot).click()
            time.sleep(1)

            from internal.infra.pages.profile_page import ProfilePage
            return ProfilePage()

        except Exception as e:
            print(f"點 pic_headshot 失败: {e}")
            pytest.xfail("點 pic_headshot 失败")

    def text_username_click(self):
        try:
            self.d(description=self.text_username).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 text_username 失败: {e}")
            pytest.xfail("點 text_username 失败")

    def comment_text_click(self):
        try:
            self.d(description=self.comment_text).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 comment_text 失败: {e}")
            pytest.xfail("點 comment_text 失败")

    def comment_media_click(self):
        try:
            self.d(description=self.comment_media).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 comment_media 失败: {e}")
            pytest.xfail("點 comment_media 失败")

    def icon_comment_click(self):
        try:
            self.d(description=self.icon_comment).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_comment 失败: {e}")
            pytest.xfail("點 icon_comment 失败")

    def icon_share_click(self):
        try:
            self.d(description=self.icon_share).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_share 失败: {e}")
            pytest.xfail("點 icon_share 失败")

    def icon_like_click(self):
        try:
            self.d(description=self.icon_unlike).click(timeout=1)

        except Exception as e:
            print(f"點 icon_like 失败: {e}")
            pytest.xfail("點 icon_like 失败")

    def icon_unlike_click(self):
        try:
            self.d(description=self.icon_like).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_unlike 失败: {e}")
            pytest.xfail("點 icon_unlike 失败")

    def icon_save_click(self):
        try:
            self.d(description=self.icon_unsave).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_save 失败: {e}")
            pytest.xfail("點 icon_save 失败")

    def icon_unsave_click(self):
        try:
            self.d(description=self.icon_save).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_unsave 失败: {e}")
            pytest.xfail("點 icon_unsave 失败")

    def icon_more_click(self):
        try:
            self.d(description=self.icon_more).click()
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
            time.sleep(1)
            if self.d(description="Tab 5 of 5").exists():
                self.d(description="Tab 5 of 5").click()
                print("成功進入 myprofile！")
                self.d(description="title_username").wait(timeout=10)
                from internal.infra.pages.profile_page import ProfilePage
                return ProfilePage()
            else:
                pytest.xfail("進入 myprofile 失败")
        except Exception as e:
            print(f"進入 myprofile 失败: {e}")
            pytest.xfail("進入 myprofile 失败")

    def explore_click(self):
        try:
            time.sleep(1)
            if self.d(description="Tab 3 of 5").exists(timeout=3):
                self.d(description="Tab 3 of 5").click()
                print("成功進入 explore！")
                from internal.infra.pages.explore import Explore
                return Explore()

        except Exception as e:
            print(f"進入 explore 失败: {e}")
            pytest.xfail("進入 explore 失败")

    def ai_click(self):
        try:
            time.sleep(1)
            if self.d(description="Tab 3 of 5").exists():
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
            time.sleep(1)
            if self.d(description="Tab 2 of 5").exists(timeout=3):
                self.d(description="Tab 2 of 5").click()
                print("成功進入spot！")
                self.d(description="icon_create").wait(timeout=10)
                from internal.infra.pages.spotfeed import SpotFeed
                return SpotFeed()
        except Exception as e:
            print(f"進入spot失败: {e}")
            pytest.xfail("進入spot失败")

    def community_click(self):
        try:
            time.sleep(1)
            if self.d(description="Tab 1 of 5").exists(timeout=3):
                self.d(description="Tab 1 of 5").click()
                print("成功進入community！")
                self.d(description="text_communityname").wait(timeout=10)
                from internal.infra.pages.spotfeed import SpotFeed
                return SpotFeed()
        except Exception as e:
            print(f"進入 community 失败: {e}")
            pytest.xfail("進入 community 失败")

    def tab_notifications_click(self):
        try:
            if self.d(description="Tab 4 of 5").exists(timeout=3):
                self.d(description="Tab 4 of 5").click()
                print("成功進入 tab_notifications！")
                from internal.infra.pages.notifications import Notifications
                return Notifications()
        except Exception as e:
            print(f"進入 tab_notifications 失败: {e}")
            pytest.xfail("進入 tab_notifications 失败")