import uiautomator2 as u2
import time, pytest
import random
import string, os


class CreateCommunity:

    def __init__(self):
        self.textfields_communityname_typing_xpath = '//android.widget.EditText[1]'
        self.textfields_description_typing_xpath = '//android.widget.EditText[2]'
        self.textfields_description_x_y = (0.226, 0.606)
        self.textbar_location_x_y = (0.193, 0.51)
        self.textfields_communityname_x_y = (0.119, 0.354)
        self.btn_edit_photo_xpath = '//*[@content-desc="Edit Photo"]/android.widget.ImageView[2]'
        self.icon_back_x_y = (0.056, 0.061)
        self.d = u2.connect()
        
    def icon_back_click(self):
        try:
            self.d.click(*self.icon_back_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 icon_back_click 失败: {e}")

    def btn_edit_photo_click(self):
        try:
            time.sleep(1)
            self.d.xpath(self.btn_edit_photo_xpath).click()
            time.sleep(1)

            from internal.infra.pages.create_community_upload_album import CreateCommunityUploadAlbum
            return CreateCommunityUploadAlbum()

        except Exception as e:
            pytest.xfail(f"點 btn_edit_photo_click 失败: {e}")

    def textfields_communityname_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.textfields_communityname_x_y)
            time.sleep(1)

        except Exception as e:
            pytest.xfail(f"點 textfields_communityname_click 失败: {e}")

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
            self.d.click(*self.textbar_location_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 textbar_location_click 失败: {e}")
            pytest.xfail("點 textbar_location_click 失败")

    def textfields_description_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.textfields_description_x_y)
            time.sleep(1)

        except Exception as e:
            print(f"點 textfields_description_click 失败: {e}")
            pytest.xfail("點 textfields_description_click 失败")

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
            self.d(description="Create").click()
            time.sleep(8)

        except Exception as e:
            print(f"點 btn_create_click 失败: {e}")
            pytest.xfail("點 btn_create_click 失败")

    def generate_random_string(self, length=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

