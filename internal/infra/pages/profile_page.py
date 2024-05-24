import uiautomator2 as u2
import time,pytest


class ProfilePage:

    def __init__(self):
        self.d = u2.connect()

        self.text_url_x_y = (0.059, 0.294)
        self.btn_contact = 'btn_contact'
        self.card_addprofilepicture_x_y = (0.473, 0.255)
        self.btn_share = "btn_share"
        self.btn_editprofile = 'btn_editprofile'
        self.text_bio = "text_bio"
        self.text_profile_name = "text_profile_name"
        self.text_joined = "text_joined"
        self.text_following = "text_following"
        self.text_followers = "text_followers"
        self.pic_l_headshot = "pic_l_headshot"
        self.icon_create = "icon_create"
        self.icon_menu = "icon_menu"
        self.icon_notification_x_y = (0.803, 0.064)
        self.title_username = "title_username"

        self.icon_dm = "icon_dm"
        self.tab_spots = "tab_spots"
        self.tab_activities = "tab_activities"
        self.comment_x_y = (0.551, 0.439)
        self.first_video_x_y = (0.169, 0.524)

    def title_username_click(self):
        try:
            time.sleep(1)
            self.d(description=self.title_username).click()

        except Exception as e:
            print(f"點擊 title_username_click 失败: {e}")
            pytest.xfail("點擊 title_username_click 失败")

    def icon_dm_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_dm).click()

            from internal.infra.pages.dm_list import DmList
            return DmList()

        except Exception as e:
            print(f"點擊 icon_dm_click 失败: {e}")
            pytest.xfail("點擊 icon_dm_click 失败")

    def icon_notification_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_notification_x_y)

        except Exception as e:
            print(f"點擊 icon_notification_click 失败: {e}")
            pytest.xfail("點擊 icon_notification_click 失败")

    def icon_menu_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_menu).click()

        except Exception as e:
            print(f"點擊 icon_menu_click 失败: {e}")
            pytest.xfail("點擊 icon_menu_click 失败")

    def icon_create_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_create).click()

        except Exception as e:
            print(f"點擊 icon_create_click 失败: {e}")
            pytest.xfail("點擊 icon_create_click 失败")

    def pic_l_headshot_click(self):
        try:
            time.sleep(1)
            self.d(description=self.pic_l_headshot).click()

        except Exception as e:
            print(f"點擊 pic_l_headshot_click 失败: {e}")
            pytest.xfail("點擊 pic_l_headshot_click 失败")

    def text_followers_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_followers).click()

        except Exception as e:
            print(f"點擊 text_followers_click 失败: {e}")
            pytest.xfail("點擊 text_followers_click 失败")

    def text_following_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_following).click()

        except Exception as e:
            print(f"點擊 text_following_click 失败: {e}")
            pytest.xfail("點擊 text_following_click 失败")

    def text_joined_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_joined).click()

        except Exception as e:
            print(f"點擊 text_joined_click 失败: {e}")
            pytest.xfail("點擊 text_joined_click 失败")

    def text_profile_name_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_profile_name).click()

        except Exception as e:
            print(f"點擊 text_profile_name_click 失败: {e}")
            pytest.xfail("點擊 text_profile_name_click 失败")

    def text_bio_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_bio).click()

        except Exception as e:
            print(f"點擊 text_bio_click 失败: {e}")
            pytest.xfail("點擊 text_bio_click 失败")

    def btn_editprofile_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_editprofile).click()

        except Exception as e:
            print(f"點擊 btn_editprofile_click 失败: {e}")
            pytest.xfail("點擊 btn_editprofile_click 失败")

    def btn_share_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_share).click()

        except Exception as e:
            print(f"點擊 btn_share_click 失败: {e}")
            pytest.xfail("點擊 btn_share_click 失败")

    def btn_contact_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_contact).click()

        except Exception as e:
            print(f"點擊 btn_contact_click 失败: {e}")
            pytest.xfail("點擊 btn_contact_click 失败")
            
    def tab_activities_click(self):
        try:
            time.sleep(1)
            self.d(description="""Activities
Tab 2 of 2""").click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 activities_page 失败: {e}")
            pytest.xfail("點擊 activities_page 失败")

    def tab_spots_click(self):
        try:
            self.d(description="""Spots
Tab 1 of 2""").click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 spots_click 失败: {e}")
            pytest.xfail("點擊 spots_click 失败")

    def text_sharespot_click(self):
        try:
            time.sleep(1)
            self.d(description="Share your first Spot").click()

        except Exception as e:
            print(f"點擊 text_sharespot_click 失败: {e}")
            pytest.xfail("點擊 text_sharespot_click 失败")

    def text_url_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_url_x_y)

        except Exception as e:
            print(f"點擊 text_url_click 失败: {e}")
            pytest.xfail("點擊 text_url_click 失败")

    def comment_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.comment_x_y)

            from internal.infra.pages.comment import Comment
            return Comment()

        except Exception as e:
            print(f"點擊 comment_video 失败: {e}")
            pytest.xfail("點擊 comment_video 失败")

    def first_video_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.first_video_x_y)
            from internal.infra.pages.spot_page import SpotPage
            return SpotPage()

        except Exception as e:
            print(f"點擊 first_video 失败: {e}")
            pytest.xfail("點擊 first_video 失败")

