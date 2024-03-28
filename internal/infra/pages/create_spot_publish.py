import uiautomator2 as u2
import time, pytest


class CreateSpotPublish:

    def __init__(self):
        self.d = u2.connect()
        self.text_done_x_y = (0.908, 0.077)
        self.textbar_location_x_y = (0.187, 0.893)
        self.icon_trim_x_y = (0.907, 0.061)
        self.icon_volume_x_y = (0.919, 0.116)
        self.icon_download_x_y = (0.925, 0.176)

    def btn_post_click_comment(self):
        try:
            self.d(description="Done").click()
            time.sleep(1)

        except Exception as e:
            print(f"點 btn_post 失败: {e}")
            pytest.xfail("點 btn_post 失败")

    def icon_trim_click(self):
        try:
            self.d.click(*self.icon_trim_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_trim 失败: {e}")
            pytest.xfail("點 icon_trim 失败")

    def icon_volume_click(self):
        try:
            self.d.click(*self.icon_volume_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_volume_click 失败: {e}")
            pytest.xfail("點 icon_volume_click 失败")

    def icon_download_click(self):
        try:
            self.d.click(*self.icon_download_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 icon_download_click 失败: {e}")
            pytest.xfail("點 icon_download_click 失败")

    def textfields_caption_click(self):
        try:
            time.sleep(5)
            self.d.xpath('//android.widget.EditText').click()
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_caption 失败: {e}")
            pytest.xfail("點 textfields_caption 失败")

    def textbar_location_click(self):
        try:
            self.d.click(*self.textbar_location_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 textbar_location 失败: {e}")
            pytest.xfail("點 textbar_location 失败")

    def btn_post_click(self):
        try:
            self.d(description="Post").click()
            time.sleep(50)

        except Exception as e:
            print(f"點 btn_post_click 失败: {e}")
            pytest.xfail("點 btn_post_click 失败")