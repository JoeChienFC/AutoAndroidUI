import uiautomator2 as u2
import time,pytest


class YearsOldPopUp:

    def __init__(self):
        self.d = u2.connect()

    def pop_up_13_years_old(self):
        try:
            if self.d(description="Yes").exists(2):
                self.d(description="Yes").click()
                print("按掉13Y彈窗")
                time.sleep(1)
        except Exception as e:
            print(f"按掉13Y彈窗失败: {e}")
            pytest.xfail("按掉13Y彈窗失败")


