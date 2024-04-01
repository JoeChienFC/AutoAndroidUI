import uiautomator2 as u2
import time,pytest


class Menu:

    def __init__(self):
        self.list_settings_x_y = (0.157, 0.564)
        self.list_switchaccount_x_y = (0.16, 0.498)
        self.list_addfriends_x_y = (0.163, 0.434)
        self.list_comments_x_y = (0.16, 0.37)
        self.list_liked_x_y = (0.169, 0.31)
        self.list_collected_x_y = (0.169, 0.247)
        self.list_account_x_y = (0.175, 0.184)
        self.back_icon_x_y = (0.059, 0.06)
        self.d = u2.connect()
        self.first_community_x_y = (0.479, 0.448)

    def icon_back_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.back_icon_x_y)

        except Exception as e:
            print(f"點擊 back_icon 失败: {e}")
            pytest.xfail("點擊 back_icon 失败")

    def icon_moon_s_click(self):
        try:
            time.sleep(1)
            self.d(className="android.widget.ImageView", index=1).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 icon_moon_s_click 失败: {e}")
            pytest.xfail("點擊 icon_moon_s_click 失败")

    def list_account_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_account_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_account_click 失败: {e}")
            pytest.xfail("點擊 list_account_click 失败")

    def list_collected_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_collected_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_collected_click 失败: {e}")
            pytest.xfail("點擊 list_collected_click 失败")

    def list_liked_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_liked_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_liked_click 失败: {e}")
            pytest.xfail("點擊 list_liked_click 失败")

    def list_comments_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_comments_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_comments_click 失败: {e}")
            pytest.xfail("點擊 list_comments_click 失败")

    def list_addfriends_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_addfriends_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_addfriends_click 失败: {e}")
            pytest.xfail("點擊 list_addfriends_click 失败")

    def list_switchaccount_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_switchaccount_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_switchaccount_click 失败: {e}")
            pytest.xfail("點擊 list_switchaccount_click 失败")

    def list_settings_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.list_settings_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點擊 list_settings_click 失败: {e}")
            pytest.xfail("點擊 list_settings_click 失败")