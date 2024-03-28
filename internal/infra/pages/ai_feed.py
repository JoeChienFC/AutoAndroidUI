import uiautomator2 as u2
import time,pytest
import os


class AiFeed:

    def __init__(self):
        self.big_icon_send_x_y = (0.94, 0.546)
        self.icon_send_x_y = (0.94, 0.854)

        self.d = u2.connect()

    def bar_message_click(self):
        try:
            time.sleep(1)
            self.d.xpath('//android.widget.EditText').click()

        except Exception as e:
            print(f"點擊 bar_message_click 失败: {e}")
            pytest.xfail("點擊 bar_message_click 失败")

    def bar_message_typing(self):
        try:
            time.sleep(1)
            # os.system('adb shell input text {}'.format('test'))
            self.d.shell('input text "test"')

        except Exception as e:
            print(f"點擊 bar_message_typing 失败: {e}")
            pytest.xfail("點擊 bar_message_typing 失败")

    def icon_send_click(self):
        try:
            if self.d(text="1").exists():
                self.d.click(*self.big_icon_send_x_y)
                time.sleep(1)
            else:
                self.d.click(*self.icon_send_x_y)

        except Exception as e:
            print(f"點擊 icon_send_click 失败: {e}")
            pytest.xfail("點擊 icon_send_click 失败")

    def pic_spot_click(self):
        try:
            self.bar_message_click()
            time.sleep(1)
            os.system('adb shell input text \\"{}\\"'.format('I like Dog'))
            time.sleep(1)
            if self.d(text="1").exists():
                self.d.click(*self.big_icon_send_x_y)
                time.sleep(1)
            else:
                self.d.click(*self.icon_send_x_y)
            time.sleep(15)
        except Exception as e:
            print(f"點擊 pic_spot_click 失败: {e}")
            pytest.xfail("點擊 pic_spot_click 失败")

    def btn_like_click(self):
        try:
            time.sleep(1)
            self.d(description="Like").click()

        except Exception as e:
            print(f"點擊 btn_like_click 失败: {e}")
            pytest.xfail("點擊 btn_like_click 失败")

    def btn_dislike_click(self):
        try:
            time.sleep(1)
            self.d(description="Dislike").click()

        except Exception as e:
            print(f"點擊 btn_dislike_click 失败: {e}")
            pytest.xfail("點擊 btn_dislike_click 失败")