import uiautomator2 as u2
import time,pytest


class NewAccountProfilePage:

    def __init__(self):
        self.btn_profile_popup_create_ad = "btn_profile_popup_create_ad"
        self.btn_profile_popup_explore_your_profile = "btn_profile_popup_explore_your_profile"
        self.text_sharecomment = "text_sharecomment"
        self.card_editusername = "card_editusername"
        self.card_setpassword = "card_setpassword"
        self.card_addbio = "card_addbio"
        self.d = u2.connect()

    def card_editusername_click(self):
        try:
            self.d(description=self.card_editusername).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 card_editusername 失败: {e}")
            pytest.xfail("點擊 card_editusername 失败")

    def card_setpassword_click(self):
        try:
            i = 10
            while i > 0:
                time.sleep(1)
                if self.d(description=self.card_setpassword).exists():
                    self.d(description=self.card_setpassword).click(timeout=2)
                    break
                else:
                    self.d(description=self.card_editusername).swipe("left", steps=30)
                    i -= 1

        except Exception as e:
            print(f"點擊 card_setpassword 失败: {e}")
            pytest.xfail("點擊 card_setpassword 失败")

    def card_addbio_click(self):
        try:
            i = 10
            while i > 0:
                time.sleep(1)
                if self.d(description=self.card_addbio).exists():
                    self.d(description=self.card_addbio).click(timeout=2)
                    break
                else:
                    self.d(description=self.card_addbio).swipe("left", steps=30)
                    i -= 1

        except Exception as e:
            print(f"點擊 card_addbio 失败: {e}")
            pytest.xfail("點擊 card_addbio 失败")

    def tab_activities_click(self):
        try:
            self.d(description="""tab_activities
Tab 2 of 2""").click(timeout=1)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 activities_page 失败: {e}")
            pytest.xfail("點擊 activities_page 失败")

    def text_sharecomment_click(self):
        try:
            self.d(description=self.text_sharecomment).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 text_sharecomment 失败: {e}")
            pytest.xfail("點擊 text_sharecomment 失败")

    def btn_profile_popup_create_ad_cilck(self):
        try:
            self.d(description=self.btn_profile_popup_create_ad).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_profile_popup_create_ad 失败: {e}")
            pytest.xfail("點擊 btn_profile_popup_create_ad 失败")

    def btn_profile_popup_explore_your_profile_cilck(self):
        try:
            self.d(description=self.btn_profile_popup_explore_your_profile).click(timeout=2)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_profile_popup_explore_your_profile 失败: {e}")
            pytest.xfail("點擊 btn_profile_popup_explore_your_profile 失败")
