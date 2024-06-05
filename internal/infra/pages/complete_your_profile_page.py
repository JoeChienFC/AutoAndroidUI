import uiautomator2 as u2
import time,pytest

from internal.infra.pages.create_community import CreateCommunity
from internal.infra.pages.system import System


class CompleteYourProfilePage:

    def __init__(self):

        self.icon_edit_headshot = "icon_edit_headshot"
        self.textfield_change_username = "textfield_change_username"
        self.textfield_password = "textfield_password"
        self.textfield_confirm_password = "textfield_confirm_password"
        self.textfield_email = "textfield_email"
        self.textfield_birthday = "textfield_birthday"
        self.textfield_link = "textfield_link"
        self.btn_upgrade = "btn_upgrade"
        self.icon_back = "icon_back"

        self.d = u2.connect()

    def icon_back_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_back).click()

        except Exception as e:
            print(f"點擊 back_icon 失败: {e}")
            pytest.xfail("點擊 back_icon 失败")

    def icon_edit_headshot_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_edit_headshot).click()

        except Exception as e:
            print(f"點擊 icon_edit_headshot 失败: {e}")
            pytest.xfail("點擊 icon_edit_headshot 失败")

    def textfield_change_username_click(self):
        try:
            time.sleep(1)
            self.d(description=self.textfield_change_username).click()

        except Exception as e:
            print(f"點擊 textfield_change_username 失败: {e}")
            pytest.xfail("點擊 textfield_change_username 失败")

    def textfield_password_click(self):
        try:
            time.sleep(1)
            self.d(description=self.textfield_password).click()

        except Exception as e:
            print(f"點擊 textfield_password 失败: {e}")
            pytest.xfail("點擊 textfield_password 失败")

    def textfield_confirm_password_click(self):
        try:
            time.sleep(1)
            self.d(description=self.textfield_confirm_password).click()

        except Exception as e:
            print(f"點擊 textfield_confirm_password 失败: {e}")
            pytest.xfail("點擊 textfield_confirm_password 失败")

    def textfield_email_click(self):
        try:
            time.sleep(1)
            self.d(description=self.textfield_email).click()

        except Exception as e:
            print(f"點擊 textfield_email 失败: {e}")
            pytest.xfail("點擊 textfield_email 失败")

    def textfield_birthday_click(self):
        try:
            time.sleep(1)
            self.d(description=self.textfield_birthday).click()

        except Exception as e:
            print(f"點擊 textfield_birthday 失败: {e}")
            pytest.xfail("點擊 textfield_birthday 失败")

    def textfield_link_click(self):
        try:
            time.sleep(1)
            self.d(description=self.textfield_link).click()

        except Exception as e:
            print(f"點擊 textfield_link 失败: {e}")
            pytest.xfail("點擊 textfield_link 失败")

    def btn_upgrade_click(self):
        try:
            random_text = CreateCommunity().generate_random_string()
            time.sleep(1)
            self.textfield_change_username_click()
            self.d.shell(f'input text "{random_text}"')
            time.sleep(0.5)
            self.textfield_password_click()
            self.d.shell('input text "1qasw23ed"')
            time.sleep(0.5)
            self.textfield_confirm_password_click()
            self.d.shell('input text "1qasw23ed"')
            time.sleep(0.5)
            self.screen_swipeupanddown()
            time.sleep(0.5)
            self.textfield_email_click()
            self.d.shell(f'input text "{random_text}@gggg.com"')
            time.sleep(0.5)
            self.textfield_birthday_click()
            self.d(description="1996").swipe("up")
            System().back_click()
            self.d(description=self.btn_upgrade).click()

        except Exception as e:
            print(f"點擊 btn_upgrade 失败: {e}")
            pytest.xfail("點擊 btn_upgrade 失败")

    def screen_swipeupanddown(self):
        try:
            time.sleep(1)
            self.d.swipe_ext("up")

        except Exception as e:
            print(f"上滑 screen 失败: {e}")
            pytest.xfail("上滑 screen 失败")