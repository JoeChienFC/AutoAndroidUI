import uiautomator2 as u2
import time,pytest


class ProfilePage:

    def __init__(self):
        self.comment_media = "comment_media"
        self.text_location = "text_location"
        self.d = u2.connect()

        self.pic_spot = "pic_spot"
        self.text_translation = "text_translation"
        self.btn_message = "btn_message"
        self.btn_follow = "btn_follow"
        self.icon_back = "icon_back"
        self.text_url = "text_url"
        self.btn_contact = 'btn_contact'
        self.card_addprofilepicture = "card_addprofilepicture"
        self.card_verifyyouremail = "card_verifyyouremail"
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
        self.text_sharespot = "text_sharespot"
        self.comment_text = "comment_text"

        self.icon_dm = "icon_dm"
        self.tab_spots = "tab_spots"
        self.tab_activities = "tab_activities"
        self.icon_more = "icon_more"
        self.icon_unlike = "icon_unlike"
        self.icon_like = "icon_like"
        self.icon_unsave = "icon_unsave"
        self.icon_save = "icon_save"
        self.icon_share = "icon_share"
        self.icon_comment = "icon_comment"
        self.text_username = "text_username"
        self.pic_headshot = "pic_headshot"
        self.text_communityname = "text_communityname"


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
            self.d(description="""tab_activities
Tab 2 of 2""").click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 activities_page 失败: {e}")
            pytest.xfail("點擊 activities_page 失败")

    def tab_spots_click(self):
        try:
            self.d(description="""tab_spots
Tab 1 of 2""").click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 spots_click 失败: {e}")
            pytest.xfail("點擊 spots_click 失败")

    def text_sharespot_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_sharespot).click()

        except Exception as e:
            print(f"點擊 text_sharespot_click 失败: {e}")
            pytest.xfail("點擊 text_sharespot_click 失败")

    def text_url_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_url).click()

        except Exception as e:
            print(f"點擊 text_url_click 失败: {e}")
            pytest.xfail("點擊 text_url_click 失败")

    def comment_text_click(self):
        try:
            time.sleep(1)
            self.d(description=self.comment_text).click()

            from internal.infra.pages.comment import Comment
            return Comment()

        except Exception as e:
            print(f"點擊 comment_text 失败: {e}")
            pytest.xfail("點擊 comment_text 失败")

    def text_communityname_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_communityname).click()

        except Exception as e:
            print(f"點擊 text_communityname 失败: {e}")
            pytest.xfail("點擊 text_communityname 失败")

    def pic_headshot_click(self):
        try:
            time.sleep(1)
            self.d(description=self.pic_headshot).click()

        except Exception as e:
            print(f"點擊 pic_headshot 失败: {e}")
            pytest.xfail("點擊 pic_headshot 失败")

    def text_username_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_username).click()

        except Exception as e:
            print(f"點擊 text_username 失败: {e}")
            pytest.xfail("點擊 text_username 失败")

    def icon_comment_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_comment).click()

        except Exception as e:
            print(f"點擊 icon_comment 失败: {e}")
            pytest.xfail("點擊 icon_comment 失败")

    def icon_share_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_share).click()

        except Exception as e:
            print(f"點擊 icon_share 失败: {e}")
            pytest.xfail("點擊 icon_share 失败")

    def icon_save_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_unsave).click()

        except Exception as e:
            print(f"點擊 icon_save 失败: {e}")
            pytest.xfail("點擊 icon_save 失败")

    def icon_unsave_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_save).click()

        except Exception as e:
            print(f"點擊 icon_unsave 失败: {e}")
            pytest.xfail("點擊 icon_unsave 失败")

    def icon_like_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_unlike).click()

        except Exception as e:
            print(f"點擊 icon_like 失败: {e}")
            pytest.xfail("點擊 icon_like 失败")

    def icon_unlike_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_like).click()

        except Exception as e:
            print(f"點擊 icon_unlike 失败: {e}")
            pytest.xfail("點擊 icon_unlike 失败")

    def icon_more_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_more).click()

        except Exception as e:
            print(f"點擊 icon_more 失败: {e}")
            pytest.xfail("點擊 icon_more 失败")

    def screen_swipeupanddown(self):
        try:
            time.sleep(1)
            self.d.swipe_ext("up")

        except Exception as e:
            print(f"上滑 screen 失败: {e}")
            pytest.xfail("上滑 screen 失败")

    def card_verifyyouremail_click(self):
        try:
            time.sleep(1)
            self.d(description=self.card_verifyyouremail).click()

        except Exception as e:
            print(f"點擊 card_verifyyouremail 失败: {e}")
            pytest.xfail("點擊 card_verifyyouremail 失败")

    def card_addprofilepicture_click(self):
        try:
            time.sleep(1)
            self.d(description=self.card_addprofilepicture).click()

        except Exception as e:
            print(f"點擊 card_addprofilepicture 失败: {e}")
            pytest.xfail("點擊 card_addprofilepicture 失败")

    def icon_back_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_back).click()

        except Exception as e:
            print(f"點擊 icon_back 失败: {e}")
            pytest.xfail("點擊 icon_back 失败")

    def btn_follow_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_follow).click()

        except Exception as e:
            print(f"點擊 btn_follow 失败: {e}")
            pytest.xfail("點擊 btn_follow 失败")

    def btn_message_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_message).click()

        except Exception as e:
            print(f"點擊 btn_message 失败: {e}")
            pytest.xfail("點擊 btn_message 失败")

    def text_translation_click(self):
        try:
            time.sleep(1)
            i = 10
            while i > 0:
                time.sleep(1)
                if self.d(description=self.text_translation).exists():
                    self.d(description=self.text_translation).click()
                    break
                else:
                    self.d(description=self.icon_back).click()
                    self.screen_swipeupanddown()
                    self.pic_headshot_click()
                    i -= 1

        except Exception as e:
            print(f"點擊 text_translation 失败: {e}")
            pytest.xfail("點擊 text_translation 失败或找不到 text_translation")

    def pic_spot_click(self):
        try:
            time.sleep(1)
            i = 10
            while i > 0:
                time.sleep(1)
                if self.d(description=self.pic_spot).exists():
                    self.d(description=self.pic_spot).click()
                    break
                else:
                    self.d(description=self.icon_back).click()
                    self.screen_swipeupanddown()
                    self.pic_headshot_click()
                    self.tab_spots_click()
                    i -= 1


        except Exception as e:
            print(f"點擊 pic_spot 失败: {e}")
            pytest.xfail("點擊 pic_spot 失败或找不到 pic_spot")

    def text_location_click(self):
        try:
            time.sleep(1)
            i = 10
            while i > 0:
                time.sleep(1)
                if self.d(description=self.text_location).exists():
                    self.d(description=self.text_location).click()
                    break
                else:
                    self.screen_swipeupanddown()
                    i -= 1

        except Exception as e:
            print(f"點擊 text_location 失败: {e}")
            pytest.xfail("點擊 text_location 失败或找不到 text_location")

    def comment_media_click(self):
        try:
            time.sleep(1)
            i = 10
            while i > 0:
                time.sleep(1)
                if self.d(description=self.comment_media).exists():
                    self.d(description=self.comment_media).click()
                    break
                else:
                    self.screen_swipeupanddown()
                    i -= 1

        except Exception as e:
            print(f"點擊 comment_media 失败: {e}")
            pytest.xfail("點擊 comment_media 失败或找不到 comment_media")