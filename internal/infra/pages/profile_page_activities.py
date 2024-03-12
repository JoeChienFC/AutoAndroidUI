import uiautomator2 as u2
import time


class ProfilePageActivities:

    def __init__(self):
        self.d = u2.connect()
        self.community_x_y = (0.17, 0.409)

    def community_click(self):
        try:
            time.sleep(1)
            self.d.click(*self.community_x_y)
            from internal.infra.pages.community_comment_page import CommunityCommentPage
            return CommunityCommentPage()

        except Exception as e:
            print(f"點擊 community 失败: {e}")
            assert False, "點擊 community 失败"

