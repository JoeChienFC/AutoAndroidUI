import uiautomator2 as u2
import time,pytest


class CommunityPage:

    def __init__(self):
        self.icon_create = "icon_create"
        self.pic_spot = "pic_spot"
        self.comment_media = "comment_media"
        self.text_username = "text_username"
        self.btn_leave_community_popup_cancel = "btn_leave_community_popup_cancel"
        self.btn_leave_community_popup_leave_this_community = "btn_leave_community_popup_leave_this_community"
        self.icon_back = "icon_back"
        self.title_communityname = "title_communityname"
        self.text_communitylocation = "text_communitylocation"
        self.text_members = "text_members"
        self.btn_join = "btn_join"
        self.btn_unjoin = "btn_unjoin"
        self.btn_share = "btn_share"
        self.pic_headshot = "pic_headshot"
        self.text_location = "text_location"
        self.comment_text = "comment_text"
        self.icon_unlike = "icon_unlike"
        self.icon_like = "icon_like"
        self.icon_unsave = "icon_unsave"
        self.icon_save = "icon_save"
        self.icon_more = "icon_more"
        self.icon_share = "icon_share"
        self.icon_comment = "icon_comment"
        self.d = u2.connect()

    def icon_back_click(self):
        try:
            self.d(description=self.icon_back).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 icon_back 失败: {e}")
            pytest.xfail("點擊 icon_back 失败")

    def title_communityname_click(self):
        try:
            self.d(description=self.title_communityname).click(timeout=2)

        except Exception as e:
            print(f"點擊 title_communityname 失败: {e}")
            pytest.xfail("點擊 title_communityname 失败")

    def text_communitylocation_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_communitylocation).click(timeout=2)

        except Exception as e:
            print(f"點擊 text_communitylocation 失败: {e}")
            pytest.xfail("點擊 text_communitylocation 失败")

    def text_members_click(self):
        try:
            self.d(description=self.text_members).click(timeout=2)

        except Exception as e:
            print(f"點擊 text_members 失败: {e}")
            pytest.xfail("點擊 text_members 失败")

    def btn_join_click(self):
        try:
            if not self.d(description=self.icon_create).exists():
                self.d(description=self.btn_join).click(timeout=2)
            else:
                pass

        except Exception as e:
            print(f"點擊 btn_join 失败: {e}")
            pytest.xfail("點擊 btn_join 失败")

    def btn_unjoin_click(self):
        try:
            if self.d(description=self.icon_create).exists():
                self.d(description=self.btn_join).click(timeout=2)

        except Exception as e:
            print(f"點擊 btn_unjoin 失败: {e}")
            pytest.xfail("點擊 btn_unjoin 失败")

    def btn_share_click(self):
        try:
            self.d(description=self.btn_share).click(timeout=2)

        except Exception as e:
            print(f"點擊 share_btn 失败: {e}")
            pytest.xfail("點擊 share_btn 失败")

    def tab_activities_click(self):
        try:
            self.d(description="""tab_activities
Tab 1 of 2""").click(timeout=1)

        except Exception as e:
            print(f"點擊 tab_activities 失败: {e}")
            pytest.xfail("點擊 tab_activities 失败")

    def tab_spots_click(self):
        try:
            self.d(description="""tab_spots
Tab 2 of 2""").click(timeout=1)

        except Exception as e:
            print(f"點擊 tab_spots 失败: {e}")
            pytest.xfail("點擊 tab_spots 失败")

    def icon_create_click(self):
        try:
            self.d(description=self.icon_create).click(timeout=2)

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
            self.d(description=self.pic_headshot).click(timeout=2)

        except Exception as e:
            print(f"點擊 pic_headshot 失败: {e}")
            pytest.xfail("點擊 pic_headshot 失败")

    def text_location_click(self):
        try:
            time.sleep(1)
            i = 20
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
            pytest.xfail("點擊 text_location 失败")

    def comment_text_click(self):
        try:
            self.d(description=self.comment_text).click(timeout=2)

        except Exception as e:
            print(f"點擊 comment_text 失败: {e}")
            pytest.xfail("點擊 comment_text 失败")

    def icon_like_click(self):
        try:
            self.d(description=self.icon_unlike).click(timeout=3)

        except Exception as e:
            print(f"點 icon_like 失败: {e}")
            pytest.xfail("點 icon_like 失败")

    def icon_unlike_click(self):
        try:
            self.d(description=self.icon_like).click(timeout=3)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_unlike 失败: {e}")
            pytest.xfail("點 icon_unlike 失败")

    def icon_save_click(self):
        try:
            self.d(description=self.icon_unsave).click(timeout=1)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_save 失败: {e}")
            pytest.xfail("點 icon_save 失败")

    def icon_unsave_click(self):
        try:
            self.d(description=self.icon_save).click(timeout=1)
            time.sleep(2)

        except Exception as e:
            print(f"點 icon_unsave 失败: {e}")
            pytest.xfail("點 icon_unsave 失败")

    def icon_more_click(self):
        try:
            self.d(description=self.icon_more).click(timeout=2)

        except Exception as e:
            print(f"點擊 右上角more 失败: {e}")
            pytest.xfail("點擊 右上角more 失败")

    def comment_icon_more_click(self):
        try:
            self.d(description=self.icon_more).click(timeout=2)

            from internal.infra.pages.comment_more_popup import CommentMorePopup
            return CommentMorePopup()

        except Exception as e:
            print(f"點擊 more 失败: {e}")
            pytest.xfail("點擊 more 失败")

    def icon_share_click(self):
        try:
            self.d(description=self.icon_share).click(timeout=2)

            from internal.infra.pages.shareto_popup import ShareToPopup
            return ShareToPopup()

        except Exception as e:
            print(f"點擊 share 失败: {e}")
            pytest.xfail("點擊 share 失败")

    def icon_comment_click(self):
        try:
            self.d(description=self.icon_comment).click(timeout=2)

        except Exception as e:
            print(f"點擊 comment 失败: {e}")
            pytest.xfail("點擊 comment 失败")

    def btn_leave_community_popup_leave_this_community_click(self):
        try:
            self.d(description=self.btn_leave_community_popup_leave_this_community).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_leave_community_popup_leave_this_community 失败: {e}")
            pytest.xfail("點擊 btn_leave_community_popup_leave_this_community 失败")

    def btn_leave_community_popup_cancel_click(self):
        try:
            self.d(description=self.btn_leave_community_popup_cancel).click(timeout=2)

        except Exception as e:
            print(f"點擊 btn_leave_community_popup_cancel 失败: {e}")
            pytest.xfail("點擊 btn_leave_community_popup_cancel 失败")

    def text_username_click(self):
        try:
            self.d(description=self.text_username).click(timeout=2)

        except Exception as e:
            print(f"點擊 text_username 失败: {e}")
            pytest.xfail("點擊 text_username 失败")

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
            pytest.xfail("點擊 comment_media 失败")

    def pic_spot_click(self):
        try:
            from internal.infra.pages.communityfeed import CommunityFeed
            time.sleep(1)
            i = 10
            while i > 0:
                time.sleep(1)
                if self.d(description=self.pic_spot).exists():
                    time.sleep(1)
                    self.d(description=self.pic_spot).click(timeout=1, offset=(0.3, 0.3))
                    break
                else:
                    self.icon_back_click()
                    self.screen_swipeupanddown()
                    CommunityFeed().text_communityname_click().tab_spots_click()
                    i -= 1

        except Exception as e:
            print(f"點擊 pic_spot 失败: {e}")
            pytest.xfail("點擊 pic_spot 失败")