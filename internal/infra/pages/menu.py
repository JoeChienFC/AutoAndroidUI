import uiautomator2 as u2
import time,pytest


class Menu:

    def __init__(self):
        self.icon_back = "icon_back"
        self.icon_moon_s = "icon_moon_s"
        self.icon_moon_f = "icon_moon_f"
        self.list_upgradeaccount = "list_upgradeaccount"
        self.list_account = "list_account"
        self.list_collected = "list_collected"
        self.list_liked = "list_liked"
        self.list_comments = "list_comments"
        self.list_addfriends = "list_addfriends"
        self.list_switchaccount = "list_switchaccount"
        self.list_settings = "list_settings"

        self.d = u2.connect()

    def icon_back_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_back).click()

        except Exception as e:
            print(f"點擊 back_icon 失败: {e}")
            pytest.xfail("點擊 back_icon 失败")

    def icon_moon_s_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_moon_s).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 icon_moon_s_click 失败: {e}")
            pytest.xfail("點擊 icon_moon_s_click 失败")

    def icon_moon_f_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_moon_f).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 icon_moon_f_click 失败: {e}")
            pytest.xfail("點擊 icon_moon_f_click 失败")

    def list_upgradeaccount_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_upgradeaccount).click()
            time.sleep(1)
            from internal.infra.pages.get_an_official_account_page import GetAnOfficialAccountPage
            return GetAnOfficialAccountPage()

        except Exception as e:
            print(f"點擊 list_upgradeaccount 失败: {e}")
            pytest.xfail("點擊 list_upgradeaccount 失败")

    def list_account_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_account).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_account_click 失败: {e}")
            pytest.xfail("點擊 list_account_click 失败")

    def list_collected_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_collected).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_collected_click 失败: {e}")
            pytest.xfail("點擊 list_collected_click 失败")

    def list_liked_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_liked).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_liked_click 失败: {e}")
            pytest.xfail("點擊 list_liked_click 失败")

    def list_comments_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_comments).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_comments_click 失败: {e}")
            pytest.xfail("點擊 list_comments_click 失败")

    def list_addfriends_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_addfriends).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_addfriends_click 失败: {e}")
            pytest.xfail("點擊 list_addfriends_click 失败")

    def list_switchaccount_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_switchaccount).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_switchaccount_click 失败: {e}")
            pytest.xfail("點擊 list_switchaccount_click 失败")

    def list_settings_click(self):
        try:
            time.sleep(1)
            self.d(description=self.list_settings).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_settings_click 失败: {e}")
            pytest.xfail("點擊 list_settings_click 失败")

