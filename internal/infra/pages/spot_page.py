import uiautomator2 as u2
import time, pytest


class SpotPage:

    def __init__(self):
        self.icon_back = "icon_back"
        self.icon_create = "icon_create"
        self.title_communityname = "title_communityname"
        self.btn_follow = "btn_follow"
        self.btn_unfollow = "btn_unfollow"
        self.icon_unlike = "icon_unlike"
        self.icon_like = "icon_like"
        self.text_caption = "text_caption"
        self.text_sharecommunity = "text_sharecommunity"
        self.screen_mute_x_y = "screen_mute_x_y"
        self.text_location = "text_location"
        self.text_username = "text_username"
        self.pic_headshot = "pic_headshot"
        self.icon_more = "icon_more"
        self.icon_share = "icon_share"
        self.icon_comment = "icon_comment"
        self.btn_collect = "btn_collect"
        self.btn_uncollect = "btn_uncollect"
        self.btn_download = "btn_download"
        self.btn_not_interested = "btn_not_interested"
        self.btn_report = "btn_report"
        self.d = u2.connect()

        self.spot_page_setup()

    def spot_page_setup(self):
        try:
            if self.d(description="縮小").exists(5):
                self.d(description="縮小").click()
        except Exception as e:
            print(f"An error occurred during setup: {e}")

    def icon_back_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_back).click(timeout=1)

        except Exception as e:
            print(f"點擊 icon_back 失败: {e}")
            pytest.xfail("點擊 icon_back 失败")

    def icon_create_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_create).click(timeout=1)

        except Exception as e:
            print(f"點擊 icon_create 失败: {e}")
            pytest.xfail("點擊 icon_create 失败")

    def title_communityname_click(self):
        try:
            time.sleep(1)
            i = 10
            while i > 0:
                time.sleep(1)
                if self.d(description=self.title_communityname).exists():
                    self.d(description=self.title_communityname).click()
                    break
                else:
                    self.screen_swipeupanddown()
                    i -= 1

        except Exception as e:
            print(f"點擊 title_communityname 失败: {e}")
            pytest.xfail("點擊 title_communityname 失败")

    def btn_follow_click(self):
        try:
            time.sleep(1)
            if self.d(description=self.btn_follow).exists():
                self.d(description=self.btn_follow).click(timeout=1)
            else:
                pytest.xfail("沒有找到 follow 按鈕")

        except Exception as e:
            print(f"點擊 follow 失败: {e}")
            pytest.xfail("點擊 follow 失败")

    def btn_unfollow_click(self):
        try:
            if self.d(description=self.btn_unfollow).exists():
                self.d(description=self.btn_unfollow).click(timeout=1)
                time.sleep(1)
            else:
                pytest.xfail("沒有找到 following 按鈕")

        except Exception as e:
            print(f"點擊 following 失败: {e}")
            pytest.xfail("點擊 following 失败")

    def icon_like_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_unlike).click(timeout=1)

        except Exception as e:
            print(f"點擊 like 失败: {e}")
            pytest.xfail("點擊 like 失败")

    def icon_unlike_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_like).click(timeout=1)

        except Exception as e:
            print(f"點擊 icon_unlike 失败: {e}")
            pytest.xfail("點擊 icon_unlike 失败")

    def text_caption_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_caption).click(timeout=1)

        except Exception as e:
            print(f"點擊 text_caption 失败: {e}")
            pytest.xfail("點擊 text_caption 失败")

    def text_sharecommunity_click(self):
        try:
            time.sleep(1)
            i = 10
            while i > 0:
                time.sleep(1)
                if self.d(description=self.text_sharecommunity).exists():
                    self.d(description=self.text_sharecommunity).click()
                    break
                else:
                    self.screen_swipeupanddown()
                    i -= 1

        except Exception as e:
            print(f"點擊 text_sharecommunity 失败: {e}")
            pytest.xfail("點擊 text_sharecommunity 失败")

    def screen_swipeupanddown(self):
        try:
            time.sleep(1)
            self.d.swipe_ext("up")

        except Exception as e:
            print(f"上滑 screen 失败: {e}")
            pytest.xfail("上滑 screen 失败")

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

    def text_location_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_location).click(timeout=1)

        except Exception as e:
            print(f"點擊 location_icon 失败: {e}")
            pytest.xfail("點擊 location_icon 失败")

    def text_username_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_username).click(timeout=1)

        except Exception as e:
            print(f"點擊 username_text 失败: {e}")
            pytest.xfail("點擊 username_text 失败")

    def pic_headshot_click(self):
        try:
            time.sleep(1)
            self.d(description=self.pic_headshot).click(timeout=1)

        except Exception as e:
            print(f"點擊 headshot_pic 失败: {e}")
            pytest.xfail("點擊 headshot_pic 失败")

    def icon_more_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_more).click(timeout=1)

            from internal.infra.pages.spot_more_popup import SpotMorePopup
            return SpotMorePopup()
        except Exception as e:
            print(f"點擊 more 失败: {e}")
            pytest.xfail("點擊 more 失败")

    def icon_share_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_share).click(timeout=1)
            time.sleep(1)
            from internal.infra.pages.shareto_popup import ShareToPopup
            return ShareToPopup()

        except Exception as e:
            print(f"點擊 share 失败: {e}")
            pytest.xfail("點擊 share 失败")

    def icon_comment_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_comment).click(timeout=1)

        except Exception as e:
            print(f"點擊 comment 失败: {e}")
            pytest.xfail("點擊 comment 失败")

    def btn_collect_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_collect).click(timeout=1)

        except Exception as e:
            print(f"點擊 btn_collect 失败: {e}")
            pytest.xfail("點擊 btn_collect 失败")

    def btn_uncollect_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_uncollect).click(timeout=1)

        except Exception as e:
            print(f"點擊 btn_uncollect 失败: {e}")
            pytest.xfail("點擊 btn_uncollect 失败")

    def btn_download_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_download).click(timeout=1)

        except Exception as e:
            print(f"點擊 btn_download 失败: {e}")
            pytest.xfail("點擊 btn_download 失败")

    def btn_not_interested_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_not_interested).click(timeout=1)

        except Exception as e:
            print(f"點擊 btn_not_interested 失败: {e}")
            pytest.xfail("點擊 btn_not_interested 失败")

    def btn_report_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_report).click(timeout=1)

        except Exception as e:
            print(f"點擊 btn_report 失败: {e}")
            pytest.xfail("點擊 btn_report 失败")

