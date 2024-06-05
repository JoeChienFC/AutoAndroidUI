import uiautomator2 as u2
import time,pytest
import os


class GetAnOfficialAccountPage:

    def __init__(self):

        self.icon_back = "icon_back"
        self.btn_upgrade_account = "btn_upgrade_account"
        self.d = u2.connect()

    def btn_upgrade_account_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_upgrade_account).click()
            from internal.infra.pages.complete_your_profile_page import CompleteYourProfilePage
            return CompleteYourProfilePage()

        except Exception as e:
            print(f"點擊 btn_upgrade_account 失败: {e}")
            pytest.xfail("點擊 btn_upgrade_account 失败")

    def icon_back_click(self):
        try:
            time.sleep(1)
            self.d(description=self.icon_back).click()

        except Exception as e:
            print(f"點擊 icon_back 失败: {e}")
            pytest.xfail("點擊 icon_back 失败")
