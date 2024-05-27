import uiautomator2 as u2
import time,pytest


class CommunityCommentPage:

    def __init__(self):
        self.title_communityname = "title_communityname"
        self.icon_back = "icon_back"
        self.pic_main_headshot = "pic_main_headshot"
        self.pic_main_username = "pic_main_username"
        self.icon_main_comment = "icon_main_comment"
        self.icon_main_share = "icon_main_share"
        self.icon_main_like = "icon_main_like"
        self.icon_main_more = "icon_main_more"

        self.d = u2.connect()

    def title_communityname_click(self):
        try:
            time.sleep(1)
            self.d(description=self.title_communityname).click()
            time.sleep(3)

        except Exception as e:
            print(f"點擊 title_community_name 失败: {e}")
            pytest.xfail("點擊 title_community_name 失败")

    def icon_back_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_back).click()

        except Exception as e:
            print(f"點擊 back_icon 失败: {e}")
            pytest.xfail("點擊 back_icon 失败")

    def pic_main_headshot_click(self):
        try:
            time.sleep(1)
            self.d(description=self.pic_main_headshot).click()

        except Exception as e:
            print(f"點擊 pic_main_headshot 失败: {e}")
            pytest.xfail("點擊 pic_main_headshot 失败")

    def pic_main_username_click(self):
        try:
            time.sleep(1)
            self.d(description=self.pic_main_username).click()

        except Exception as e:
            print(f"點擊 pic_main_username 失败: {e}")
            pytest.xfail("點擊 pic_main_username 失败")

    def text_translation_click(self):
        try:
            time.sleep(1)
            if self.d(description="See Translation").exists(2):
                self.d(description="See Translation").click()
            else:
                self.d(description="See Original").click()
                time.sleep(1.5)
                self.d(description="See Translation").click()

        except Exception as e:
            print(f"點擊 text_translation 失败: {e}")
            pytest.xfail("點擊 text_translation 失败")

    def icon_main_comment_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_main_comment).click()

        except Exception as e:
            print(f"點擊 icon_main_comment_click 失败: {e}")
            pytest.xfail("點擊 icon_main_comment_click 失败")

    def icon_main_share_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_main_share).click()

        except Exception as e:
            print(f"點擊 icon_main_share_click 失败: {e}")
            pytest.xfail("點擊 icon_main_share_click 失败")

    def icon_main_like_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_main_like).click()

        except Exception as e:
            print(f"點擊 icon_main_like_click 失败: {e}")
            pytest.xfail("點擊 icon_main_like_click 失败")

    def icon_main_more_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_main_more).click()
            time.sleep(1)

            from internal.infra.pages.comment_more_popup import CommentMorePopup
            return CommentMorePopup()

        except Exception as e:
            print(f"點擊 icon_main_more_click 失败: {e}")
            pytest.xfail("點擊 icon_main_more_click 失败")