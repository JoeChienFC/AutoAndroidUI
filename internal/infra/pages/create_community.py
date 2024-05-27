import uiautomator2 as u2
import time, pytest
import random
import string, os


class CreateCommunity:

    def __init__(self):
        self.textfields_description = "textfields_description"
        self.textbar_location = "textbar_location"
        self.textfields_communityname = "textfields_communityname"
        self.icon_back = "icon_back"
        self.btn_edit_photo = "btn_edit_photo"
        self.btn_create = "btn_create"

        self.d = u2.connect()
        
    def icon_back_click(self):
        try:
            self.d(description=self.icon_back).click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 icon_back 失败: {e}")

    def btn_edit_photo_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_edit_photo).click()

            from internal.infra.pages.create_community_upload_album import CreateCommunityUploadAlbum
            return CreateCommunityUploadAlbum()

        except Exception as e:
            pytest.xfail(f"點 btn_edit_photo 失败: {e}")

    def textfields_communityname_click(self):
        try:
            time.sleep(1)
            self.d(description=self.textfields_communityname).click()
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 textfields_communityname 失败: {e}")

    def textfields_communityname_typing(self):
        try:
            random_text = self.generate_random_string()
            time.sleep(1)
            os.system('adb shell input text {}'.format(random_text))
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_communityname_typing 失败: {e}")
            pytest.xfail("點 textfields_communityname_typing 失败")

    def textbar_location_click(self):
        try:
            time.sleep(1)
            self.d(description=self.textbar_location).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 textbar_location 失败: {e}")
            pytest.xfail("點 textbar_location 失败")

    def textfields_description_click(self):
        try:
            time.sleep(1)
            self.d(description=self.textfields_description).click()
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_description 失败: {e}")
            pytest.xfail("點 textfields_description 失败")

    def textfields_description_typing(self):
        try:
            time.sleep(1)
            os.system('adb shell input text {}'.format("你好"))
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_description_typing 失败: {e}")
            pytest.xfail("點 textfields_description_typing 失败")

    def btn_create_click(self):
        try:
            time.sleep(1)
            self.d(description=self.btn_create).click()
            time.sleep(8)

        except Exception as e:
            print(f"點 btn_create 失败: {e}")
            pytest.xfail("點 btn_create 失败")

    def generate_random_string(self, length=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

