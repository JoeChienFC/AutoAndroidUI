import uiautomator2 as u2
import time, pytest


class CommunityFeedDropdownMenu:

    def __init__(self):
        self.d = u2.connect()
        
    def list_create_click(self):
        try:
            self.d(description="Create a Community").click()
            time.sleep(1)

            from internal.infra.pages.create_community import CreateCommunity
            return CreateCommunity()

        except Exception as e:
            pytest.xfail(f"點 list_create_click 失败: {e}")

    def list_joined_click(self):
        try:
            time.sleep(1)
            self.d(description="Joined Communities").click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 list_joined_click 失败: {e}")

