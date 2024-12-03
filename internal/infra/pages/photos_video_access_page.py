import uiautomator2 as u2
import time, pytest
import os


class PhotosVideoAccessPage:

    def __init__(self):
        self.d = u2.connect()

    def enable_access_click(self):
        try:
            if self.d(resourceId="com.nothing.gallery:id/bottom_hint").exists():
                self.d(resourceId="com.nothing.gallery:id/bottom_hint").click()
                time.sleep(1)
            pass

        except Exception as e:
            print(f"點擊 enable_access_click 失败: {e}")
            pytest.xfail("點擊 enable_access_click 失败")

    def allow_all_click(self):
        try:
            if self.d(text="Allow all").exists():
                self.d(text="Allow all").click()
                time.sleep(1)
            pass

        except Exception as e:
            print(f"點擊 allow_all_click 失败: {e}")
            pytest.xfail("點擊 allow_all_click 失败")
