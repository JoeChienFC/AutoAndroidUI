import uiautomator2 as u2
import time, pytest
import os


class ShowInPhotosViewPage:

    def __init__(self):
        self.d = u2.connect()

    def is_screenshots_select(self):
        select = self.d(resourceId="com.nothing.gallery:id/display_name", text="Screenshots").right(
            resourceId='com.nothing.gallery:id/switch_widget', selected='true')

        if not select:
            pytest.fail("screenshots 選項没有被選中")

    def is_not_favorites_select(self):
        if not self.d(text="Favourite").exists(timeout=3):
            pytest.fail("沒有 Favourite 選項")
        select = self.d(resourceId="com.nothing.gallery:id/display_name", text="Favourite").right(
            resourceId='com.nothing.gallery:id/switch_widget', selected='false')

        if not select:
            pytest.fail("Favourite 選項有被選中")

    def is_not_video_select(self):
        if not self.d(text="Video").exists(timeout=3):
            pytest.fail("沒有 Video 選項")
        select = self.d(resourceId="com.nothing.gallery:id/display_name", text="Video").right(
            resourceId='com.nothing.gallery:id/switch_widget', selected='false')

        if not select:
            pytest.fail("Video 選項有被選中")

    def video_select(self):
        no_select = self.d(resourceId="com.nothing.gallery:id/display_name", text="Video").right(
            resourceId='com.nothing.gallery:id/switch_widget', selected='false')
        if no_select:
            self.d(resourceId="com.nothing.gallery:id/display_name", text="Video").click()
