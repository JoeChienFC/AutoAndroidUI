import uiautomator2 as u2
import time

class CommunityFeed:

    def __init__(self):
        self.d = u2.connect()

    def enable_community_info(self):
        try:
            if self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]').exists:
                self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[2]').click()
                print("成功開啟community_info！")
                time.sleep(10)
        except Exception as e:
            print(f"開啟community_info失败: {e}")
            assert False, "開啟community_info失败"

    def update_community_feed(self):
        width, height = self.d.window_size()

        # 定义起始和结束坐标，模拟下拉刷新操作
        start_x = width // 2
        start_y = height // 4
        end_y = height * 3 // 4

        # 模拟手指下滑操作
        self.d.swipe(start_x, start_y, start_x, end_y)

        # 等待一段时间以确保页面加载完成
        time.sleep(30)  # 根据需要调整等待时间

    def update_community_info(self):
        time.sleep(3)
        if self.d(description="Tab 1 of 5").exists(5):
            self.d(description="Tab 1 of 5").click()
        if self.d(description="Tab 2 of 5").exists(5):
            self.d(description="Tab 2 of 5").click()

    def click_first_community(self):
        self.d.xpath('//android.widget.ScrollView/android.view.View[1]/android.view.View[1]/android.view.View[1]').exists_click(5)
