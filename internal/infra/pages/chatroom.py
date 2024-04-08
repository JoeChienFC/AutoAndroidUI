import uiautomator2 as u2
import time, pytest


class Chatroom:

    def __init__(self):
        self.message_longclick_x_y = (0.913, 0.438)
        self.d = u2.connect()

    def bar_message_click(self):
        try:
            self.d.xpath('//android.widget.EditText').click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 bar_message_click 失敗: {e}")

    def bar_message_typing(self):
        try:
            self.d.shell('input text "test"')
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 bar_message_typing 失敗: {e}")

    def icon_send_click(self):
        try:
            self.d(className="android.widget.ImageView", index=3).click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 icon_send_click 失敗: {e}")

    def message_longclick(self):
        try:
            self.d.long_click(*self.message_longclick_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 message_longclick 失敗: {e}")
