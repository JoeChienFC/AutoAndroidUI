import time

import pytest

from internal.infra.adb.adb_function import ADBClient
from internal.infra.pages.albums_page import AlbumsPage
from internal.infra.pages.create_album_popup import CreateAlbumPopup
from internal.infra.pages.general_page import GeneralPage
from internal.infra.pages.photos_page import PhotosPage
from internal.infra.pages.select_photo_video_page import SelectPhotoVideoPage


@pytest.mark.P0
def test_gallery_albums_001():
    """
    打开Gallery应用，进入相簿页面
    步骤：
    "1.点击“建立”按钮(右上更多按鈕裡面)。
    2.不輸入相簿名称并点击“确定”
    3.输入新的相簿名称并点击“确定”。
    4.選擇放入相片"
    期望结果：
    "2.“确定”反灰無法点击
    4.成功创建新相簿，页面显示新建相簿。"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_1_pic", "Camera")
    ADBClient.refresh_gallery_media()

    GeneralPage().btn_albums_click().btn_more_options_click().btn_create_click().btn_ok_click()
    CreateAlbumPopup().is_ok_btn_gray()
    CreateAlbumPopup().send_keys("test")
    CreateAlbumPopup().btn_ok_click().photo_video_select()
    SelectPhotoVideoPage().btn_finish_click().btn_move_click()
    AlbumsPage().check_album_count("test", "1")


@pytest.mark.P0
def test_gallery_albums_003():
    """
    打开Gallery应用，进入相簿页面
    步骤：
    "1.点击“新建相簿”按钮。
    2.输入新的相簿名称并点击“确定”。
    3.重复步骤1和2，输入已有的相簿名称并点击“确定”。"
    期望结果：
    "3.显示紅色错误提示，不能创建重复名称的相簿。
    英文(There's already an album with that name)"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_albums()
    ADBClient.refresh_gallery_media()

    GeneralPage().btn_albums_click().btn_more_options_click().btn_create_click().send_keys("data_albums")
    CreateAlbumPopup().btn_ok_click()
    CreateAlbumPopup().is_texts_exists("There's already an album with that name.")

