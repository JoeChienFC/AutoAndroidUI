import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.api.get_bi_api import API
from internal.infra.pages.communityfeed import CommunityFeed

'''
1. 啟動應用程式並導覽至主頁（Homefeed）。
2. 開啟「Community Info」。
3. 在首頁（Homefeed）點擊「Community Feed」以刷新社群內容。
4. 使用 adb logcat 輸入類型 1408 並從日誌中取得頂部的社群 ID。
5. 呼叫 API 取得預設視圖計數。
6. 等待從 adb logcat 無法檢索到類型 1408 的日誌資訊。
7. 在首頁（Homefeed）點擊「Community Feed」以刷新社群內容。
8. 呼叫 API 以取得新的視圖計數。
9. 檢查新的視圖計數是否等於預設視圖計數 + 1。
'''


def test_action_type_1408():
    ADBClient.start_playsee_app().enter_community().enable_community_info()
    communityid = update_community_get_community_id()
    assert communityid is not None, "未找到 community_id。"

    default_view_count = API.get_api_community_result_view_count(communityid)
    print(f"default view:{default_view_count}")

    ADBClient.clean_action_type_1408()
    new_view_count, times = update_community_get_community_view_count(communityid)
    print(f"update : {times} ")
    print(f"new view:{new_view_count}")
    assert default_view_count + 1 == new_view_count, "view_count 沒有增加"


def update_community_get_community_view_count(community_id):
    community_feed = CommunityFeed()
    times = 0
    for i in range(10):
        if not ADBClient.check_action_type_1408_is_none():
            time.sleep(10)
            view_count = API.get_api_community_result_view_count(community_id)
            return view_count, times
        else:
            community_feed.update_community_info()
            times += 1
            time.sleep(7)


def update_community_get_community_id():
    community_feed = CommunityFeed()
    for iteration in range(100):
        community_feed.update_community_info()
        communityid = ADBClient.logcat_action_type_1408_community_id()
        if communityid is not None:
            print(f"找到 community_id: {communityid}")
            return communityid
