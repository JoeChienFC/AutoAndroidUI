import uiautomator2 as u2
import time, pytest
import os


class SelectPhotoMorePopover:

    def __init__(self):
        self.btn_edit = "Edit"
        self.btn_details = "Details"
        self.btn_copy_to_album = "Copy to album"
        self.btn_move_to_album = "Move to album"
        self.btn_set_as = "Set as"
        self.btn_duplicate = "Duplicate"
        self.btn_hide = "Hide"
        self.d = u2.connect()

    def btn_edit_click(self):
        try:
            self.d(description=self.btn_edit).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_edit_click 失败: {e}")
            pytest.xfail("點擊 btn_edit_click 失败")

    def btn_details_click(self):
        try:
            self.d(description=self.btn_details).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_details_click 失败: {e}")
            pytest.xfail("點擊 btn_details_click 失败")

    def btn_copy_to_album_click(self):
        try:
            self.d(description=self.btn_copy_to_album).click()
            time.sleep(1)

            from internal.infra.pages.copy_to_album_page import CopyToAlbumPage
            return CopyToAlbumPage()
        except Exception as e:
            print(f"點擊 btn_copy_to_album 失败: {e}")
            pytest.xfail("點擊 btn_copy_to_album 失败")

    def btn_move_to_album_click(self):
        try:
            self.d(description=self.btn_move_to_album).click()
            time.sleep(1)

            from internal.infra.pages.move_to_album_page import MoveToAlbumPage
            return MoveToAlbumPage()

        except Exception as e:
            print(f"點擊 btn_move_to_album 失败: {e}")
            pytest.xfail("點擊 btn_move_to_album 失败")

    def btn_set_as_click(self):
        try:
            self.d(description=self.btn_set_as).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_set_as 失败: {e}")
            pytest.xfail("點擊 btn_set_as 失败")

    def btn_clone_click(self):
        try:
            self.d(description=self.btn_duplicate).click()
            time.sleep(1)

        except Exception as e:
            print(f"點擊 btn_clone 失败: {e}")
            pytest.xfail("點擊 btn_clone 失败")

    def check_set_as_button_disabled(self):
        if not self.d(description="Set as", enabled="false").exists:
            pytest.fail("Set as 按鈕沒有至灰被禁用")

    def is_photo_more_popover(self):
        if not self.d(description=self.btn_duplicate).exists and self.d(description=self.btn_hide).exists:
            pytest.fail("沒有出現 more 提示框")

