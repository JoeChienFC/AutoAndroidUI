import uiautomator2 as u2
import time

from internal.infra.pages.communityfeed import CommunityFeed


class HomeFeed:

    def __init__(self):
        self.d = u2.connect()
        self.location_picker_xpath = '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]'

    def location_picker_click(self):
        try:
            if self.d(description="縮小").exists(5):
                self.d(description="縮小").click()
            # 點擊 location picker
            self.d.xpath(self.location_picker_xpath).click()

        except Exception as e:
            print(f"進入 location_picker 失败: {e}")
            assert False, "進入 location_picker 失败"

    def enter_community(self):

        try:
            if self.d(description="Tab 2 of 5").exists(5):
                self.d(description="Tab 2 of 5").click()
                print("成功進入community！")
                time.sleep(10)
                return CommunityFeed()
        except Exception as e:
            print(f"進入community失败: {e}")
            assert False, "進入community失败"

    def enter_ailex_page(self):

        try:
            if self.d(description="Tab 3 of 5").exists(5):
                self.d(description="Tab 3 of 5").click()
                print("成功進入Ailex page！")
                time.sleep(10)
                # return CommunityFeed()
        except Exception as e:
            print(f"進入Ailex page失败: {e}")
            assert False, "進入Ailex page失败"

    def enter_search_page(self):

        try:
            if self.d(description="Tab 4 of 5").exists(5):
                self.d(description="Tab 4 of 5").click()
                print("成功進入Search page！")
                time.sleep(10)
                # return CommunityFeed()
        except Exception as e:
            print(f"進入Search page失败: {e}")
            assert False, "進入Search page失败"

    def enter_my_profile_page(self):

        try:
            if self.d(description="Tab 5 of 5").exists(5):
                self.d(description="Tab 5 of 5").click()
                print("成功進入My Profile page！")
                time.sleep(5)
                # return CommunityFeed()
        except Exception as e:
            print(f"進入My Profile page失败: {e}")
            assert False, "進入My Profile page失败"
    def swipe_up_next_post(self):

        try:
            self.d.swipe_ext("up")
            print("成功上滑！")
            time.sleep(1)
            # return CommunityFeed()
        except Exception as e:
            print(f"上滑失败: {e}")
            assert False, "上滑失败"

    def swipe_down_previous_post(self):

        try:
            self.d.swipe_ext("down")
            print("成功下滑！")
            time.sleep(1)
            # return CommunityFeed()
        except Exception as e:
            print(f"下滑失败: {e}")
            assert False, "下滑失败"

    def click_like(self):

        try:
            self.d.xpath('//android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.Button[1]').click()
            print("成功點Like！")
            time.sleep(1)
            # return CommunityFeed()
        except Exception as e:
            print(f"點Like失败: {e}")
            assert False, "點Like失败"
