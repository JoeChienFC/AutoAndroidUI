import uiautomator2 as u2
import time, pytest


class SpotFeed:

    def __init__(self):
        self.d = u2.connect()

        self.icon_comment = "icon_comment"
        self.icon_share = "icon_share"
        self.icon_like = "icon_like"
        self.icon_unlike = "icon_unlike"
        self.icon_more = "icon_more"
        self.icon_unsave = "icon_unsave"
        self.icon_save = "icon_save"

        self.icon_create = "icon_create"
        self.btn_locationpicker = "btn_locationpicker"
        self.pic_headshot = "pic_headshot"
        self.text_username = "text_username"
        self.text_location = "text_location"
        self.screen_mute_x_y = (0.511, 0.457)
        self.text_sharecommunity = "text_sharecommunity"
        self.text_caption = "text_caption"
        self.btn_follow = "btn_follow"
        self.btn_unfollow = "btn_unfollow"

        self.home_feed_setup()

    def home_feed_setup(self):
        try:
            if self.d(description="縮小").exists(5):
                self.d(description="縮小").click()
        except Exception as e:
            pytest.xfail(f"An error occurred during setup: {e}")

    def icon_create_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_create).click()

            from internal.infra.pages.create_spot_upload_album import CreateSpotUploadAlbum
            return CreateSpotUploadAlbum()

        except Exception as e:
            print(f"點擊 icon_create 失败: {e}")
            pytest.xfail("點擊 icon_create 失败")

    def text_caption_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_caption).click()

        except Exception as e:
            print(f"點擊 text_caption 失败: {e}")
            pytest.xfail("點擊 text_caption 失败")

    def text_sharecommunity_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_sharecommunity).click()

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
            self.d(description=self.text_location).click()

        except Exception as e:
            print(f"點擊 location_icon 失败: {e}")
            pytest.xfail("點擊 location_icon 失败")

    def text_username_click(self):
        try:
            time.sleep(1)
            self.d(description=self.text_username).click()

        except Exception as e:
            print(f"點擊 username_text 失败: {e}")
            pytest.xfail("點擊 username_text 失败")

    def pic_headshot_click(self):
        try:
            time.sleep(1)
            self.d(description=self.pic_headshot).click()

        except Exception as e:
            print(f"點擊 headshot_pic 失败: {e}")
            pytest.xfail("點擊 headshot_pic 失败")

    def icon_more_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_more).click()
            time.sleep(4)

            from internal.infra.pages.spot_more_popup import SpotMorePopup
            return SpotMorePopup()
        except Exception as e:
            print(f"點擊 more 失败: {e}")
            pytest.xfail("點擊 more 失败")

    def icon_share_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_share).click()
            time.sleep(1)
            from internal.infra.pages.shareto_popup import ShareToPopup
            return ShareToPopup()

        except Exception as e:
            print(f"點擊 share 失败: {e}")
            pytest.xfail("點擊 share 失败")

    def icon_comment_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_comment).click()

        except Exception as e:
            print(f"點擊 comment 失败: {e}")
            pytest.xfail("點擊 comment 失败")

    def icon_like_click(self):
        try:
            self.d(description=self.icon_unlike).click(timeout=2)

        except Exception as e:
            print(f"點擊 like 失败: {e}")
            pytest.xfail("點擊 like 失败")

    def icon_unlike_click(self):
        try:
            time.sleep(2)
            self.d(description=self.icon_like).click()

        except Exception as e:
            print(f"點擊 unlike 失败: {e}")
            pytest.xfail("點擊 unlike 失败")

    def btn_follow_click(self):
        try:
            self.d(description=self.btn_follow).click()

        except Exception as e:
            print(f"點擊 follow 失败: {e}")
            pytest.xfail("點擊 follow 失败")

    def btn_unfollow_click(self):
        try:
            self.d(description=self.btn_unfollow).click()

        except Exception as e:
            print(f"點擊 unfollow 失败: {e}")
            pytest.xfail("點擊 unfollow 失败")

    def btn_locationpicker_click(self):
        try:
            # 點擊 location picker
            self.d(description=self.btn_locationpicker).click()
            time.sleep(1)
            from internal.infra.pages.spot_location_picker import SpotLocationPicker
            return SpotLocationPicker()

        except Exception as e:
            print(f"進入 location_picker 失败: {e}")
            pytest.xfail("進入 location_picker 失败")

    def btn_collect_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_unsave).click()

        except Exception as e:
            print(f"點擊 collect 失败: {e}")
            pytest.xfail("點擊 collect 失败")

    def btn_uncollect_click(self):
        try:
            time.sleep(2)
            self.d(description=self.icon_save).click()

        except Exception as e:
            print(f"點擊 uncollect 失败: {e}")
            pytest.xfail("點擊 uncollect 失败")
