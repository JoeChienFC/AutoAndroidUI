import time

import pytest

from internal.infra.adb.adb_function import ADBClient
from internal.infra.pages.general_page import GeneralPage
from internal.infra.pages.photo_all_view_page import PhotoAllViewPage
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
    ShowInPhotosViewPage().is_not_favorite_select()
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
    ADBClient.refresh_gallery_camera()

    PhotosPage().photo_click().set_as_favorite_click()
    PhotoAllViewPage().is_un_favorite_exists()

    GeneralPage().back()
    GeneralPage().btn_albums_click().is_favorite_album_has_1_img()


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
    ADBClient.refresh_gallery_camera()

    PhotosPage().photo_click().delete_click().btn_delete_click()
    PhotosPage().is_display_no_photos_text()

    GeneralPage().btn_albums_click().is_recently_deleted_album_has_1_img()


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
    ADBClient.refresh_gallery_camera()
    ADBClient.refresh_gallery_albums()

    PhotosPage().photo_click().more_click().btn_copy_to_album_click().data_albums_click()
    GeneralPage().back()
    PhotosPage().no_display_no_photos_text()

    GeneralPage().btn_albums_click().is_data_album_has_6_img()


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
    ADBClient.refresh_gallery_camera()
    ADBClient.refresh_gallery_albums()

    PhotosPage().photo_click().more_click().btn_move_to_album_click().data_albums_click()
    PhotosPage().is_display_no_photos_text()

    GeneralPage().btn_albums_click().is_data_album_has_6_img()


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
    ADBClient.refresh_gallery_camera()

    PhotosPage().photo_click().more_click().btn_clone_click()
    GeneralPage().back()
    PhotosPage().is_two_photos_exists()


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
    ADBClient.refresh_gallery_camera()

    PhotosPage().photo_click().more_click().btn_details_click()
    PhotoAllViewPage().is_location_details_correct()


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
    ADBClient.refresh_gallery_camera()

    PhotosPage().photo_click().more_click().btn_details_click()
    ADBClient.disable_auto_rotate()
    ADBClient.set_rotate()
    PhotoAllViewPage().is_location_details_correct()
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
    ADBClient.refresh_gallery_camera()
    ADBClient.disable_auto_rotate()
    ADBClient.set_rotate()

    PhotosPage().photo_click().swipe_up_to_details()
    PhotoAllViewPage().is_location_details_correct()
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
    ADBClient.refresh_gallery_camera()

    PhotosPage().photo_click().swipe_up_to_details()
    PhotoAllViewPage().is_no_location_details_correct()


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
    ADBClient.refresh_gallery_camera()
    ADBClient.disable_auto_rotate()
    ADBClient.set_rotate()

    PhotosPage().photo_click().swipe_up_to_details()
    PhotoAllViewPage().is_no_location_details_correct()
