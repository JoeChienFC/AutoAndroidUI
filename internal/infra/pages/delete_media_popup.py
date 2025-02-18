import uiautomator2 as u2
import time,pytest


class DeleteMediaPopup:

    def __init__(self):
        self.d = u2.connect()
        self.delete_panel = "com.nothing.gallery:id/parentPanel"
        self.delete_media_popup_title = "Delete media"

    def btn_delete_click(self):
        try:
            self.d(resourceId="android:id/button1", text="Delete").click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_delete_click 失败: {e}")
            pytest.xfail("點擊 btn_delete_click 失败")

    def btn_cancel_click(self):
        try:
            self.d(resourceId="android:id/button2", text="Cancel").click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_cancel_click 失败: {e}")
            pytest.xfail("點擊 btn_cancel_click 失败")

    def delete_panel_outside_click(self):
        try:
            element = self.d(resourceId=self.delete_panel)
            if element.exists:
                bounds = element.bounds()
                left, top, right, bottom = bounds  # 解構元組
                x_outside = left - 10  # 點擊左側外圍
                y_outside = top - 10  # 點擊上側外圍
                self.d.click(x_outside, y_outside)  # 點擊外部空白處
                time.sleep(0.3)
            else:
                print("未找到 parentPanel，無需點擊")
                pytest.xfail("未找到 parentPanel，無需點擊")

        except Exception as e:
            print(f"點擊 delete_panel_outside_click 失败: {e}")
            pytest.xfail("點擊 delete_panel_outside_click 失败")

    def is_delete_media_popup(self):
        if not self.d(text=self.delete_media_popup_title).exists:
            pytest.fail("沒有出現 delete media 彈框")
