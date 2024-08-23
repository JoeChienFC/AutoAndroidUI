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

