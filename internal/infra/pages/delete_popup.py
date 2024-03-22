import uiautomator2 as u2
import time,pytest


class DeletePopUp:

    def __init__(self):
        self.d = u2.connect()

    def delete_popup(self):
        try:
            print()
        except Exception as e:
            print(f"delete_popup: {e}")
            pytest.xfail("delete_popup")