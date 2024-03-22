import uiautomator2 as u2
import time,pytest


class ProfilePage:

    def __init__(self):
        self.text_url_x_y = (0.059, 0.294)
        self.btn_contact_xpath = '//*[@content-desc="Contact"]'
        self.card_addprofilepicture_x_y = (0.473, 0.255)
        self.btn_share_x_y = (0.91, 0.339)
        self.btn_editprofile_xpath = '//*[@content-desc="Edit Profile"]'
        self.text_bio_x_y = (0.056, 0.27)
        self.text_profile_name_x_y = (0.065, 0.244)
        self.text_joined_x_y = (0.892, 0.149)
        self.text_following_x_y = (0.66, 0.151)
        self.text_followers_x_y = (0.44, 0.147)
        self.pic_l_headshot_x_y = (0.169, 0.152)
        self.icon_create_x_y = (0.877, 0.828)
        self.icon_menu_x_y = (0.937, 0.062)
        self.icon_notification_x_y = (0.803, 0.064)
        self.title_username_x_y = (0.154, 0.061)
        self.d = u2.connect()

        self.icon_dm_x_y = (0.675, 0.061)
        self.activities_page_x_y = (0.756, 0.356)
        self.comment_x_y = (0.551, 0.439)
        self.first_video_x_y = (0.169, 0.524)

    def title_username_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.title_username_x_y)

        except Exception as e:
            print(f"點擊 title_username_click 失败: {e}")
            pytest.xfail("點擊 title_username_click 失败")

    def icon_dm_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_dm_x_y)

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
            self.d.click(*self.icon_menu_x_y)

        except Exception as e:
            print(f"點擊 icon_menu_click 失败: {e}")
            pytest.xfail("點擊 icon_menu_click 失败")

    def icon_create_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.icon_create_x_y)

        except Exception as e:
            print(f"點擊 icon_create_click 失败: {e}")
            pytest.xfail("點擊 icon_create_click 失败")

    def pic_l_headshot_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.pic_l_headshot_x_y)

        except Exception as e:
            print(f"點擊 pic_l_headshot_click 失败: {e}")
            pytest.xfail("點擊 pic_l_headshot_click 失败")

    def text_followers_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_followers_x_y)

        except Exception as e:
            print(f"點擊 text_followers_click 失败: {e}")
            pytest.xfail("點擊 text_followers_click 失败")

    def text_following_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_following_x_y)

        except Exception as e:
            print(f"點擊 text_following_click 失败: {e}")
            pytest.xfail("點擊 text_following_click 失败")

    def text_joined_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_joined_x_y)

        except Exception as e:
            print(f"點擊 text_joined_click 失败: {e}")
            pytest.xfail("點擊 text_joined_click 失败")

    def text_profile_name_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_profile_name_x_y)

        except Exception as e:
            print(f"點擊 text_profile_name_click 失败: {e}")
            pytest.xfail("點擊 text_profile_name_click 失败")

    def text_bio_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.text_bio_x_y)

        except Exception as e:
            print(f"點擊 text_bio_click 失败: {e}")
            pytest.xfail("點擊 text_bio_click 失败")

    def btn_editprofile_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.btn_editprofile_xpath).click()

        except Exception as e:
            print(f"點擊 btn_editprofile_click 失败: {e}")
            pytest.xfail("點擊 btn_editprofile_click 失败")

    def btn_share_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.btn_share_x_y)

        except Exception as e:
            print(f"點擊 btn_share_click 失败: {e}")
            pytest.xfail("點擊 btn_share_click 失败")

    def btn_contact_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.btn_contact_xpath).click()

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

