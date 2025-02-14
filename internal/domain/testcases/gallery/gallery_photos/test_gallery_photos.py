import time

import pytest

from internal.infra.adb.adb_function import ADBClient
from internal.infra.pages.albums_page import AlbumsPage
from internal.infra.pages.general_page import GeneralPage
from internal.infra.pages.photo_video_all_view_page import PhotoVideoAllViewPage
from internal.infra.pages.photo_more_popover import PhotoMorePopover
from internal.infra.pages.photos_page import PhotosPage
from internal.infra.pages.settings_page import SettingsPage
from internal.infra.pages.show_in_photos_view_page import ShowInPhotosViewPage


@pytest.mark.P0
def test_gallery_photos_001():
    """
    步骤：
    1.打開Gallery應用，進入照片頁面。
    2.點擊漢堡選單>settings>show in photos view
    3.檢查頁面
    期望结果：
    3.會有最愛/影片/螢幕截圖的選項
    3.1 預設只有螢幕截圖被勾選
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    PhotosPage().btn_more_options_click().btn_settings_click()
    SettingsPage().btn_show_in_photos_view_click()
    ShowInPhotosViewPage().is_not_favorites_select()
    ShowInPhotosViewPage().is_screenshots_select()
    ShowInPhotosViewPage().is_not_video_select()


@pytest.mark.P1
def test_gallery_photos_002():
    """
    步骤：
    "1.打開Gallery應用，進入照片頁面。
    2.觀察photos 頁面"
    期望结果：
    2.沒有顯示照片並顯示文案
    "No photo here, go take some photos!"
    """
    ADBClient.delete_albums_camera_data()
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    PhotosPage().is_display_no_photos_text()


@pytest.mark.P1
def test_gallery_photos_003():
    """
    步骤：
    "1.打開Gallery應用，進入照片頁面。
    2.點擊漢堡選單>settings>show in photos view
    3.開啟影片
    4.返回觀察photos"
    期望结果：
    4.只有顯示影片相簿內的影片
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_albums()
    PhotosPage().btn_more_options_click().btn_settings_click()
    SettingsPage().btn_show_in_photos_view_click()
    ShowInPhotosViewPage().video_select()
    GeneralPage().back()
    GeneralPage().back()
    PhotosPage().is_video_exists()
    PhotosPage().no_photos_exists()


@pytest.mark.P0
def test_gallery_photos_008():
    """
    步骤：
    "1.打開Gallery應用，進入照片頁面。
    2.點擊一張照片進入大圖視圖。
    3.點擊愛心icon。
    4.進入Albums 檢查照片是否添加到 favorite 相簿。"
    期望结果：
    "3.愛心icon 變成實心
    4.照片可以正常添加到 favorite 相簿。"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click().icon_favorite_click()
    PhotoVideoAllViewPage().is_un_favorite_exists()

    GeneralPage().back()
    GeneralPage().btn_albums_click().check_favorites_album_photos_count("1")


@pytest.mark.P0
def test_gallery_photos_012():
    """
    步骤：
    "1.打開Gallery應用，進入照片頁面。
    2.點擊一張照片進入大圖視圖。
    3.點擊刪除圖標。
    4.檢查照片是否被刪除並移至最近刪除資料夾。"
    期望结果：
    4.照片可以正常刪除並移至最近刪除資料夾。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_1_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click().delete_click().btn_delete_click()
    PhotosPage().is_not_photo_video_exists()
    PhotosPage().is_display_no_photos_text()

    GeneralPage().btn_albums_click().check_recently_deleted_album_photos_count("1")


@pytest.mark.P0
def test_gallery_photos_015():
    """
    步骤：
    "1.打開 Gallery 應用，進入照片頁面。
    2.點擊一張照片進入大圖視圖。
    3.點擊 more icon 中的 add to album 選項。
    4.將照片添加到指定的相簿。"
    期望结果：
    4.照片不會消失且可以正常添加到指定的相簿。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_1_pic_to_camera()
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_media()
    ADBClient.refresh_gallery_albums()

    PhotosPage().photo_video_click().more_click().btn_copy_to_album_click().data_albums_click()
    GeneralPage().back()
    PhotosPage().no_display_no_photos_text()

    GeneralPage().btn_albums_click().check_data_album_count("6")


@pytest.mark.P0
def test_gallery_photos_016():
    """
    步骤：
    "1.打開Gallery應用，進入照片頁面。
    2.點擊一張照片進入大圖視圖。
    3.點擊more icon中的move to album選項。
    4.將照片移動到指定的相簿。"
    期望结果：
    4.照片會消失且照片可以正常移動到指定的相簿。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_1_pic_to_camera()
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_media()
    ADBClient.refresh_gallery_albums()

    PhotosPage().photo_video_click().more_click().btn_move_to_album_click().data_albums_click()
    PhotosPage().is_not_photo_video_exists()
    PhotosPage().is_display_no_photos_text()

    GeneralPage().btn_albums_click().check_data_album_count("6")


@pytest.mark.P0
def test_gallery_photos_017():
    """
    步骤：
    "1.打開Gallery應用，進入照片頁面。
    2.點擊一張照片進入大圖視圖。
    3.點擊more icon中的clone選項。
    4.檢查複製出的照片跟照片位置。"
    期望结果：
    4.照片可以正常複製。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_1_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click().more_click().btn_clone_click()
    GeneralPage().back()
    GeneralPage().btn_albums_click()
    AlbumsPage().check_camera_photo_count("2")


@pytest.mark.P0
def test_gallery_photos_024_025():
    """
    至少有一张包含定位信息的照片。
    步骤：
    "1.打开Gallery应用，进入照片页面。
    2.点击一张照片进入大图视图。
    3.向上滑动照片，进入图片详情页面。
    4.检查详情页面是否显示以下信息：
    Name（文件名）
    image（图片信息）
    Device（拍摄装置）
    Capture（光圈参数）
    location（地图坐标）"
    期望结果：
    "3.向上滑动时，流畅进入图片详情页面。
    4.详情页面正确显示文件名、图片信息、拍摄装置、光圈参数和地图坐标。"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_location_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click().more_click().btn_details_click()
    PhotoVideoAllViewPage().is_location_details_correct()


@pytest.mark.P2
def test_gallery_photos_026():
    """
    至少有一张包含定位信息的照片。
    步骤：
    "1.打开Gallery应用，进入照片页面。
    2.点击一张照片进入大图视图。
    3.向上滑动照片，进入图片详情页面。
    4.橫放手機進入橫屏模式"
    期望结果：
   4.順暢轉成橫屏详情页面且正确显示文件名、图片信息、拍摄装置、光圈参数和地图坐标。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_location_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click().more_click().btn_details_click()
    ADBClient.disable_auto_rotate()
    ADBClient.set_rotate()
    PhotoVideoAllViewPage().is_location_details_correct()
    ADBClient.enable_auto_rotate()


@pytest.mark.P1
def test_gallery_photos_027():
    """
    至少有一张包含定位信息的照片。
    步骤：
    "1.打开Gallery应用，橫放手機進入橫屏模式，进入照片页面。
    2.点击一张照片进入大图视图。
    3.向上滑动照片，进入图片详情页面。
    5.检查详情页面是否显示以下信息：
    Name（文件名）
    image（图片信息）
    Device（拍摄装置）
    Capture（光圈参数）
    location（地图坐标）"
    期望结果：
    "3.向上滑动时，右邊動畫滑出图片详情页面。
    5.详情页面正确显示文件名、图片信息、拍摄装置、光圈参数和地图坐标。"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_location_pic_to_camera()
    ADBClient.refresh_gallery_media()
    ADBClient.disable_auto_rotate()
    ADBClient.set_rotate()

    PhotosPage().photo_video_click().swipe_up_to_details()
    PhotoVideoAllViewPage().is_location_details_correct()
    ADBClient.enable_auto_rotate()


@pytest.mark.P0
def test_gallery_photos_028():
    """
    至少有一张不包含定位信息的照片。
    步骤：
    "1.打开Gallery应用，进入照片页面。
    2.点击一张照片进入大图视图。
    3.向上滑动照片，进入图片详情页面。
    4.检查详情页面是否显示以下信息：
    Name（文件名）
    image（图片信息）
    Device（拍摄装置）
    Capture（光圈参数）"
    期望结果：
    "3.向上滑动时，流畅进入图片详情页面。
    4.详情页面正确显示文件名、图片信息、拍摄装置和光圈参数。"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_1_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click().swipe_up_to_details()
    PhotoVideoAllViewPage().is_no_location_details_correct()


@pytest.mark.P1
def test_gallery_photos_029():
    """
    至少有一张不包含定位信息的照片。
    步骤：
    "1.打开Gallery应用，橫放手機進入橫屏模式，进入照片页面。
    2.点击一张照片进入大图视图。
    3.向上滑动照片，进入图片详情页面。
    4.检查详情页面是否显示以下信息：
    Name（文件名）
    image（图片信息）
    Device（拍摄装置）
    Capture（光圈参数）"
    期望结果：
    "3.向上滑动时，右邊動畫滑出图片详情页面。
    4.详情页面正确显示文件名、图片信息、拍摄装置和光圈参数。"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_1_pic_to_camera()
    ADBClient.refresh_gallery_media()
    ADBClient.disable_auto_rotate()
    ADBClient.set_rotate()

    PhotosPage().photo_video_click().swipe_up_to_details()
    PhotoVideoAllViewPage().is_no_location_details_correct()


@pytest.mark.P1
def test_gallery_photos_038():
    """
    至少有多张照片。
    步骤：
    "1.打开Gallery应用，进入照片页面。
    2.點開照片，上滑检查照片是否按照时间顺序排列。"
    期望结果：
    2.照片应按时间顺序正确排列。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click().swipe_up_to_details()
    PhotoVideoAllViewPage().is_july_24_pic()
    GeneralPage().back()
    GeneralPage().back()
    PhotosPage().is_date_order_correct()


@pytest.mark.P0
def test_gallery_photos_042():
    """
    至少有多张照片。
    步骤：
    "1.在Gallery应用中长按选中的照片后，選中一張照片。
    2.点击下方第一个icon（+），选择要加入的相簿。"
    期望结果：
    2.照片不會消失且可以正常添加到指定的相簿。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_1_pic_to_camera()
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_media()
    ADBClient.refresh_gallery_albums()

    PhotosPage().photo_long_click()
    PhotosPage().icon_copy_to_album_click().data_albums_click()
    PhotosPage().no_display_no_photos_text()

    GeneralPage().btn_albums_click()
    AlbumsPage().check_data_album_count("6")


@pytest.mark.P0
def test_gallery_photos_043():
    """
    至少有多张照片。
    步骤：
    "1.在Gallery应用中长按选中的照片后，選中多張照片。
    2.点击下方第一个icon（+），选择要加入的相簿。"
    期望结果：
    2.照片不會消失且可以正常添加到指定的相簿。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_2_pic_to_camera()
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_media()
    ADBClient.refresh_gallery_albums()

    PhotosPage().photo_long_click()
    PhotosPage().no_select_click()
    PhotosPage().icon_copy_to_album_click().data_albums_click()
    PhotosPage().is_august_9_pic_exit()

    GeneralPage().btn_albums_click()
    AlbumsPage().check_data_album_count("7")


@pytest.mark.P0
def test_gallery_photos_046():
    """
    至少有多张照片。
    步骤：
    "1.在Gallery应用中长按选中的照片后，選中一張照片。
    2.点击第三个icon（删除），确认删除选定的照片。
    3.检查照片是否成功移动到“最近删除”相簿。"
    期望结果：
    3.照片成功删除并移动到“最近删除”相簿。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_1_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_long_click()
    PhotosPage().icon_delete_click().btn_delete_click()
    PhotosPage().is_display_no_photos_text()

    GeneralPage().btn_albums_click()
    AlbumsPage().check_recently_deleted_album_photos_count("1")


@pytest.mark.P0
def test_gallery_photos_047():
    """
    至少有多张照片。
    步骤：
    "1.在Gallery应用中长按选中的照片后，選中多張照片。
    2.点击第三个icon（删除），确认删除选定的照片。
    3.检查照片是否成功移动到“最近删除”相簿。"
    期望结果：
    3.照片成功删除并移动到“最近删除”相簿。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_2_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_long_click()
    PhotosPage().no_select_click()
    PhotosPage().icon_delete_click().btn_delete_click()
    PhotosPage().is_display_no_photos_text()

    GeneralPage().btn_albums_click()
    AlbumsPage().check_recently_deleted_album_photos_count("2")


@pytest.mark.P0
def test_gallery_photos_048():
    """
    至少有多张照片。
    步骤：
    "1.在Gallery应用中长按选中的照片后，選中一張照片。
    2.点击第四个icon（更多选项）點擊 move to album選項。
    3.將照片移動到指定的相簿。"
    期望结果：
    3.照片會消失且照片可以正常移動到指定的相簿。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_1_pic_to_camera()
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_media()
    ADBClient.refresh_gallery_albums()

    PhotosPage().photo_long_click()
    PhotosPage().icon_more_click().btn_move_to_album_click().data_albums_click()
    PhotosPage().is_display_no_photos_text()

    GeneralPage().btn_albums_click()
    AlbumsPage().check_data_album_count("6")


@pytest.mark.P0
def test_gallery_photos_049():
    """
    至少有多张照片。
    步骤：
   "1.在Gallery应用中长按选中的照片后，選中多張照片。
    2.点击第四个icon（更多选项）點擊 move to album選項。
    3.將照片移動到指定的相簿。"
    期望结果：
    3.照片會消失且照片可以正常移動到指定的相簿。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_2_pic_to_camera()
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_media()
    ADBClient.refresh_gallery_albums()

    PhotosPage().photo_long_click()
    PhotosPage().no_select_click()
    PhotosPage().icon_more_click().btn_move_to_album_click().data_albums_click()
    PhotosPage().is_display_no_photos_text()

    GeneralPage().btn_albums_click()
    AlbumsPage().check_data_album_count("7")


@pytest.mark.P0
def test_gallery_photos_050():
    """
    至少有多张照片。
    步骤：
    "1.在Gallery应用中长按选中的照片后，選中一張照片。
    2.点击第四个icon（更多选项）點擊clone選項。
    3.檢查複製出的照片跟照片位置。"
    期望结果：
    3.照片可以正常複製
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_1_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_long_click()
    PhotosPage().icon_more_click().btn_clone_click()
    GeneralPage().btn_albums_click()
    AlbumsPage().check_camera_photo_count("2")


@pytest.mark.P0
def test_gallery_photos_051():
    """
    至少有多张照片。
    步骤：
    "1.在Gallery应用中长按选中的照片后，選中多張照片。
    2.点击第四个icon（更多选项）點擊clone選項。
    3.檢查複製出的照片跟照片位置。"
    期望结果：
    3.照片可以正常複製
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_2_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_long_click()
    PhotosPage().no_select_click()
    PhotosPage().icon_more_click().btn_clone_click()

    GeneralPage().btn_albums_click()
    AlbumsPage().check_camera_photo_count("4")


@pytest.mark.P1
def test_gallery_photos_054():
    """
    至少有多张照片。
    步骤：
    "1.在Gallery应用中长按选中的照片后，選中多張照片。
    2.点击第四个icon（更多选项）點擊set as選項。"
    期望结果：
    2.選項反灰，點擊無反應。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_2_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_long_click()
    PhotosPage().no_select_click()
    PhotosPage().icon_more_click().btn_set_as_click()
    PhotoMorePopover().check_set_as_button_disabled()


@pytest.mark.P1
def test_gallery_photos_058():
    """
    至少有多张照片。
    步骤：
    "1.打开Gallery应用并进入Photos页面。
    2.使用双指缩放手势切换到月跟年缩图显示模式。
    3.关闭Gallery应用。
    4.重新打开Gallery应用，检查Photos页面的缩图显示模式。"
    期望结果：
    4.Gallery应用重新打开后，Photos页面的缩图显示模式与关闭前的状态一致。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_2_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().pinch_in()
    ADBClient.stop_gallery_app()
    ADBClient.start_gallery_app()
    PhotosPage().check_title("AUGUST 2024")


@pytest.mark.P0
def test_gallery_photos_059():
    """
    至少有多张照片。
    步骤：
    "1.打开Gallery应用并进入Photos页面。
    2.使用双指缩放手势切换到日显示模式。
    3.检查每日照片的缩图显示效果。"
    期望结果：
    3.每日照片的缩图显示正常，能够准确显示每一天的照片。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_2_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().check_title("9 AUGUST 2024")
    PhotosPage().check_title("23 JULY 2024")


@pytest.mark.P0
def test_gallery_photos_060():
    """
    至少有多张照片。
    步骤：
    "1.打开Gallery应用并进入Photos页面。
    2.使用双指缩放手势切换到月显示模式。
    3.检查每月照片的缩图显示效果。"
    期望结果：
    3.每月照片的缩图显示正常，能够准确显示每个月的照片。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_2_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().pinch_in()
    PhotosPage().check_title("AUGUST 2024")
    PhotosPage().check_title("JULY 2024")


@pytest.mark.P0
def test_gallery_photos_070():
    """
    Photos页面有可播放的视频文件。
    步骤：
    "1.打开Gallery应用并进入Photos页面。
    2.选择一个视频文件并打开。
    3.点击更多选项按钮，选择添加到favorites相簿"
    期望结果：
    3.檢查favorites相簿有此视频文件
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_1_video", "Camera")
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click().icon_favorite_click()
    PhotoVideoAllViewPage().is_un_favorite_exists()
    GeneralPage().back()
    GeneralPage().btn_albums_click()
    AlbumsPage().check_favorites_album_video_count("1")


@pytest.mark.P0
def test_gallery_photos_072():
    """
    Photos页面有可播放的视频文件。
    步骤：
    "1.打开Gallery应用并进入Photos页面。
    2.选择一个视频文件并打开。
    3.点击更多选项按钮，选择删除"
    期望结果：
    3.视频成功删除并移动到“最近删除”相簿。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_1_video", "Camera")
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click().delete_click().btn_delete_click()
    PhotosPage().is_display_no_photos_text()
    GeneralPage().btn_albums_click()
    AlbumsPage().check_recently_deleted_album_video_count("1")


@pytest.mark.P0
def test_gallery_photos_073():
    """
    Photos页面有可播放的视频文件。
    步骤：
    "1.打开Gallery应用并进入Photos页面。
    2.选择一个视频文件并打开。
    3.点击更多选项按钮，选择添加到任一相簿"
    期望结果：
    3.视频不會消失且可以正常添加到指定的相簿。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_1_video", "Camera")
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_media()
    ADBClient.refresh_gallery_albums()

    PhotosPage().photo_video_click().more_click().btn_copy_to_album_click().data_albums_click()
    GeneralPage().back()
    PhotosPage().no_display_no_photos_text()

    GeneralPage().btn_albums_click()
    AlbumsPage().check_data_album_video_count("2")


@pytest.mark.P0
def test_gallery_photos_074():
    """
    Photos页面有可播放的视频文件。
    步骤：
    "1.打开Gallery应用并进入Photos页面。
    2.选择一个视频文件并打开。
    3.点击更多选项按钮，选择移動到新建的相簿"
    期望结果：
    3.视频會消失且可以正常添加到指定的相簿。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_1_video", "Camera")
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_media()
    ADBClient.refresh_gallery_albums()

    PhotosPage().photo_video_click().more_click().btn_move_to_album_click().data_albums_click()
    PhotosPage().is_display_no_photos_text()

    GeneralPage().btn_albums_click()
    AlbumsPage().check_data_album_video_count("2")


@pytest.mark.P0
def test_gallery_photos_075():
    """
    Photos页面有可播放的视频文件。
    步骤：
    "1.打开Gallery应用并进入Photos页面。
    2.选择一个视频文件并打开。
    3.点击更多选项按钮，选择建立副本"
    期望结果：
    3.视频可以正常複製。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_1_video", "Camera")
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click().more_click().btn_clone_click()
    GeneralPage().back()

    GeneralPage().btn_albums_click()
    AlbumsPage().check_camera_video_count("2")


@pytest.mark.P0
def test_gallery_photos_082():
    """
    已存在連拍组照片
    步骤：
    "1.打开Gallery App并进入Photos页面。
    2.点击任意照片进入大图视图。
    3.在大图视图下方转盘中找到連拍照片堆叠。
    4.点击照片堆叠。"
    期望结果：
    "2.应用成功进入大图视图
    3.進入堆疊的照片大圖時下方转盘显示照片堆叠。
    4.点击照片堆叠后，堆叠展开，显示组内所有照片。"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_burst", "Camera")
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click()
    PhotoVideoAllViewPage().photo_click()
    PhotoVideoAllViewPage().check_filmstrip_items(5)


@pytest.mark.P1
def test_gallery_photos_083():
    """
    已存在連拍组照片
    步骤：
    "1.打开Gallery App并进入Photos页面，橫放手機進入橫屏模式。
    2.点击任意照片进入大图视图。
    3.在大图视图下方转盘中找到連拍照片堆叠。
    4.点击照片堆叠。"
    期望结果：
    "2.3.应用成功进入大图视图，并在下方转盘显示照片堆叠。
    4.点击照片堆叠后，堆叠展开，显示组内所有照片。"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_burst", "Camera")
    ADBClient.refresh_gallery_media()

    ADBClient.disable_auto_rotate()
    ADBClient.set_rotate()
    PhotosPage().photo_video_click()
    PhotoVideoAllViewPage().photo_click()
    PhotoVideoAllViewPage().check_filmstrip_items(5)


@pytest.mark.P0
def test_gallery_photos_086():
    """
    已存在連拍组照片
    步骤：
    "1.打开Gallery App并进入Photos页面。
    2.点击任意照片进入大图视图。
    3.查看大图视图下方转盘中照片堆叠的數量显示。
    4.点击堆叠组照片进行展开。"
    期望结果：
    "3.照片堆叠应显示堆叠数量（数字叠加在堆叠缩略图上）。
    4.照片數量與顯示的數字相同(例:10張的話是顯示+9)"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_burst", "Camera")
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click().is_burst_amount("+4")
    PhotoVideoAllViewPage().photo_click()
    PhotoVideoAllViewPage().check_filmstrip_items(5)


@pytest.mark.P1
def test_gallery_photos_087():
    """
    已存在連拍组照片
    步骤：
    "1.打开Gallery App并进入Photos页面，橫放手機進入橫屏模式。
    2.点击任意照片进入大图视图。
    3.查看大图视图下方转盘中照片堆叠的數量显示。
    4.点击堆叠组照片进行展开。"
    期望结果：
    "3.照片堆叠应显示堆叠数量（数字叠加在堆叠缩略图上）。
    4.照片數量與顯示的數字相同(例:10張的話是顯示+9)"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_burst", "Camera")
    ADBClient.refresh_gallery_media()

    ADBClient.disable_auto_rotate()
    ADBClient.set_rotate()
    PhotosPage().photo_video_click().is_burst_amount("+4")
    PhotoVideoAllViewPage().photo_click()
    PhotoVideoAllViewPage().check_filmstrip_items(5)


@pytest.mark.P1
def test_gallery_photos_088():
    """
    已存在連拍组照片
    步骤：
    "1.打开Gallery App并进入Photos页面。
    2.点击任意照片进入大图视图。
    3.查看大图视图下方转盘中照片堆叠的數量显示。
    4.点击堆叠组照片进行展开。
    5.刪除任一照片返回堆叠组照片"
    期望结果：
    "3.照片堆叠应显示堆叠数量（数字叠加在堆叠缩略图上）。
    4.照片數量與顯示的數字相同
    5.數量會及時顯示少1"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_burst", "Camera")
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click().is_burst_amount("+4")
    PhotoVideoAllViewPage().photo_click()
    PhotoVideoAllViewPage().delete_click().btn_delete_click()
    PhotoVideoAllViewPage().check_filmstrip_items(4)
    GeneralPage().back()
    PhotoVideoAllViewPage().is_burst_amount("+3")


@pytest.mark.P2
def test_gallery_photos_089():
    """
    已存在連拍组照片
    步骤：
    "1.打开Gallery App并进入Photos页面。
    2.点击任意照片进入大图视图。
    3.查看大图视图下方转盘中照片堆叠的數量显示。
    4.点击堆叠组照片进行展开。
    5.刪除有皇冠的封面照片"
    期望结果：
    5.會自動設定一張細節最多的照片為封面
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_burst", "Camera")
    ADBClient.refresh_gallery_media()

    PhotosPage().photo_video_click().photo_click()
    PhotoVideoAllViewPage().delete_click().btn_delete_click()
    PhotoVideoAllViewPage().check_crown_icon()


@pytest.mark.P0
def test_gallery_photos_090():
    """
    "1.已存在多組相簿
    2.相機相簿內有照片"
    步骤：
    "1.打開Gallery應用，進入照片頁面。
    2.點擊漢堡選單>settings>show in photos view
    3.關閉全部相簿
    4.返回觀察photos
    5.點擊漢堡選單>settings>show in photos view
    6.開啟任一相簿
    7.返回觀察photos"
    期望结果：
    "2.不顯示相機相簿，固定會有最愛,影片,螢幕截圖
    4.只顯示相機相簿中的相 片在photos
    7.除了相機相簿內照片，會加上顯示開啟相簿的相片"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_albums()

    PhotosPage().is_display_no_photos_text()
    PhotosPage().btn_more_options_click().btn_settings_click().btn_show_in_photos_view_click().is_camera_select()
    ShowInPhotosViewPage().albums_select("data_albums")
    GeneralPage().back()
    GeneralPage().back()
    PhotosPage().no_display_no_photos_text()


@pytest.mark.P1
def test_gallery_photos_091():
    """
    相機相簿內無照片
    步骤：
   "1.打開Gallery應用，進入照片頁面。
    2.點擊漢堡選單>settings>show in photos view
    3.關閉全部相簿
    4.返回觀察photos"
    期望结果：
    "4.沒有顯示照片並顯示文案
    "這裡沒有照片,去拍一些吧"
    "No photos here. Take your first shot"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_albums()

    PhotosPage().is_display_no_photos_text()
    PhotosPage().btn_more_options_click().btn_settings_click().btn_show_in_photos_view_click().albums_select_cancel(
        "Screenshots")
    GeneralPage().back()
    GeneralPage().back()
    PhotosPage().is_display_no_photos_text()


@pytest.mark.P2
def test_gallery_photos_092():
    """
    "1.相機相簿內無照片
    2.影片相簿內有影片"
    步骤：
   "1.打開Gallery應用，進入照片頁面。
    2.點擊漢堡選單>settings>show in photos view
    3.開啟影片
    4.返回觀察photos"
    期望结果：
    4.只有顯示影片相簿內的影片
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_albums()

    PhotosPage().is_display_no_photos_text()
    PhotosPage().btn_more_options_click().btn_settings_click().btn_show_in_photos_view_click().albums_select(
        "Video")
    GeneralPage().back()
    GeneralPage().back()
    PhotosPage().check_title("23 AUGUST 2024")


@pytest.mark.P2
def test_gallery_photos_093():
    """
    "1.已存在多組相簿
    2.設置橫屏模式"
    步骤：
    "1.打開Gallery應用，進入照片頁面。
    2.點擊漢堡選單>settings>show in photos view
    3.關閉全部相簿
    4.返回觀察photos
    5.點擊漢堡選單>settings>show in photos view
    6.開啟任一相簿
    7.返回觀察photos"
    期望结果：
    "4.沒有任何相片顯示在photos
    7.只會顯示開啟相簿的相片"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_albums()
    ADBClient.disable_auto_rotate()
    ADBClient.set_rotate()

    PhotosPage().is_display_no_photos_text()
    PhotosPage().btn_more_options_click().btn_settings_click().btn_show_in_photos_view_click().albums_select(
        "data_albums")
    GeneralPage().back()
    GeneralPage().back()
    PhotosPage().no_display_no_photos_text()


@pytest.mark.P0
def test_gallery_photos_094():
    """
    連接網路
    步骤：
    "1.打開Gallery應用，進入照片頁面。
    2.點擊漢堡選單>settings>about Gallery"
    期望结果：
    2.跳轉網頁顯示關於Gallery info
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()

    PhotosPage().btn_more_options_click().btn_settings_click().btn_about_gallery_click().is_gallery_info_html()


@pytest.mark.P2
def test_gallery_photos_095():
    """
    "1.設置橫屏模式
    2.連接網路"
    步骤：
    "1.打開Gallery應用，進入照片頁面。
    2.點擊漢堡選單>settings>about Gallery"
    期望结果：
    2.跳轉網頁顯示關於Gallery info
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.disable_auto_rotate()
    ADBClient.set_rotate()

    PhotosPage().btn_more_options_click().btn_settings_click().btn_about_gallery_click().is_gallery_info_html()


@pytest.mark.P1
def test_gallery_photos_097():
    """
开启wifi 并用手機拍一張照片(拍照需改定位权限)
    步骤：
    "1.打開Gallery應用，進入照片頁面。
    2.双指缩放进入日视图
    3.双指缩放进入月视图"
    期望结果：
    2.3. 右上角会显示拍照时定位地区
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_location_pic_to_camera()
    ADBClient.refresh_gallery_media()

    PhotosPage().check_summary("ÞINGEYJARSVEIT")
    PhotosPage().change_to_month_display()
    PhotosPage().check_summary("ÞINGEYJARSVEIT")
