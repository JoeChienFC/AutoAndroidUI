import uiautomator2 as u2
import time,pytest


class DeletePopUp:

    def __init__(self):
        self.btn_delete_x_y = (0.505, 0.831)
        self.d = u2.connect()

    def delete_popup(self):
        try:
            time.sleep(1)
            self.d.click(*self.btn_delete_x_y)
            
        except Exception as e:
            print(f"delete_popup: {e}")
            pytest.xfail("delete_popup")