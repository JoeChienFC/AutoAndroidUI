import time

import pytest

from internal.infra.adb.adb_function import ADBClient
from internal.infra.pages.albums_detail_page import AlbumDetailPage
from internal.infra.pages.albums_page import AlbumsPage
from internal.infra.pages.create_rename_album_popup import CreateRenameAlbumPopup
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
    CreateRenameAlbumPopup().is_ok_btn_gray()
    CreateRenameAlbumPopup().send_keys("test")
    CreateRenameAlbumPopup().btn_ok_click().photo_video_select()
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
    CreateRenameAlbumPopup().btn_ok_click()
    CreateRenameAlbumPopup().is_texts_exists("There's already an album with that name.")


@pytest.mark.P1
def test_gallery_albums_004():
    """
    打开Gallery应用，进入相簿页面
    步骤：
    "1.点击“新建相簿”按钮。
    2.尝试创建包含特殊字符的相簿名称并点击“确定”。"
    期望结果：
    2.成功创建包含特殊字符名称的相簿，页面显示新建相簿。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_1_pic", "Camera")
    ADBClient.refresh_gallery_media()

    GeneralPage().btn_albums_click().btn_more_options_click().btn_create_click().send_keys("!@#$%^&*()_+")
    CreateRenameAlbumPopup().btn_ok_click().photo_video_select()
    SelectPhotoVideoPage().btn_finish_click().btn_move_click()
    AlbumsPage().check_album_count("!@#$%^&*()_+", "1")


@pytest.mark.P0
def test_gallery_albums_005():
    """
    打开Gallery应用，进入相簿页面，有至少一个相簿存在
    步骤：
    "1.長按一个相簿并点击“編輯”。
    2.清除相簿名称并点击“确定”
    3.输入新的相簿名称并点击“确定”。"
    期望结果：
    "2.“确定”反灰無法点击
    3.成功改名相簿，页面显示相簿。"
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_1_pic", "Pictures")
    ADBClient.refresh_gallery_media()

    GeneralPage().btn_albums_click().albums_long_click("data_1_pic")
    AlbumsPage().icon_rename_click().clear_text()
    CreateRenameAlbumPopup().btn_ok_click()
    CreateRenameAlbumPopup().is_ok_btn_gray()
    CreateRenameAlbumPopup().send_keys("test")
    CreateRenameAlbumPopup().btn_ok_click()

    AlbumsPage().check_album_count("test", "1")


@pytest.mark.P2
def test_gallery_albums_006():
    """
    打开Gallery应用，进入相簿页面，有至少一个相簿存在
    步骤：
    "1.長按一个相簿并点击“編輯”。
    2.输入已有的相簿名称并点击“确定”。"
    期望结果：
    "3.显示紅色错误提示，不能创建重复名称的相簿。
    繁體(相簿名稱已存在)
    簡體(图集名称已存在)
    英文(There's already an album with that name)

    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_1_pic", "Pictures")
    ADBClient.push_data_to_device("data_location", "Pictures")
    ADBClient.refresh_gallery_media()

    GeneralPage().btn_albums_click().albums_long_click("data_location")
    AlbumsPage().icon_rename_click().send_keys("data_1_pic")
    CreateRenameAlbumPopup().btn_ok_click()
    CreateRenameAlbumPopup().is_texts_exists("There's already an album with that name.")


@pytest.mark.P2
def test_gallery_albums_007():
    """
    打开Gallery应用，进入相簿页面，有至少一个相簿存在
    步骤：
    "1.長按一个相簿并点击“編輯”。
    2.尝试将相簿更名为包含特殊字符的名称并点击“确定”。"
    期望结果：
    2.成功更名为包含特殊字符的名称，页面显示新的相簿名称。

    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_1_pic", "Pictures")
    ADBClient.refresh_gallery_media()

    GeneralPage().btn_albums_click().albums_long_click("data_1_pic")
    AlbumsPage().icon_rename_click().send_keys("!@#$%^&()_+")
    CreateRenameAlbumPopup().btn_ok_click()
    AlbumsPage().check_album_count("!@#$%^&()_+", "1")


@pytest.mark.P0
def test_gallery_albums_008():
    """
    "1.打开Gallery应用，进入相簿页面，有多个相簿和照片存在
    2.進入任一相簿"
    步骤：
    "1.點擊右上角新增(+)
    2.選擇非本相簿的照片或影片並點擊完成
    3.選取移動
    4.重複1-2 選取複製"
    期望结果：
    "3.該照片或影片移動至相簿(若已存在相簿內彈出提示框)
    4.該照片或影片複製至相簿"

    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_1_pic", "Pictures")
    ADBClient.push_data_to_device("data_2_pic", "Pictures")
    ADBClient.refresh_gallery_media()

    GeneralPage().btn_albums_click().enter_albums("data_1_pic").icon_add_click().photo_video_select()
    SelectPhotoVideoPage().btn_finish_click().btn_move_click()
    GeneralPage().back()
    AlbumsPage().check_album_count("data_1_pic", "2")
    AlbumsPage().check_album_count("data_2_pic", "1")
    AlbumsPage().enter_albums("data_1_pic").icon_add_click().photo_video_select()
    SelectPhotoVideoPage().btn_finish_click().btn_copy_click()
    GeneralPage().back()
    AlbumsPage().check_album_count("data_1_pic", "3")
    AlbumsPage().check_album_count("data_2_pic", "1")


@pytest.mark.P1
def test_gallery_albums_010():
    """
    "1.打开Gallery应用，进入相簿页面，有多个相簿和照片存在
    2.進入任一相簿"
    步骤：
    "1.照片長按選取一张并点击“搬移至相簿”。
    2.选择目标相簿并确认搬移。
    3.照片長按选择多张照片并点击“搬移至相簿”。
    4.选择目标相簿并确认搬移。"
    期望结果：
    "2.成功搬移单张照片，目标相簿显示该照片。
    4.成功搬移多张照片，目标相簿显示这些照片。"

    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.push_data_to_device("data_1_pic", "Pictures")
    ADBClient.push_data_to_device("data_100", "Pictures")
    ADBClient.refresh_gallery_media()

    GeneralPage().btn_albums_click().enter_albums("data_100").photo_long_click()
    AlbumDetailPage().icon_more_click().btn_move_to_album_click().select_albums_click("data_1_pic")
    GeneralPage().back()
    AlbumsPage().check_album_count("data_1_pic", "2")
    AlbumsPage().check_album_count("data_100", "99")
    AlbumsPage().enter_albums("data_100").photo_long_click()
    SelectPhotoVideoPage().photo_video_multiple_selection(2)
    AlbumDetailPage().icon_more_click().btn_move_to_album_click().select_albums_click("data_1_pic")
    GeneralPage().back()
    AlbumsPage().check_album_count("data_1_pic", "5")
    AlbumsPage().check_album_count("data_100", "96")

