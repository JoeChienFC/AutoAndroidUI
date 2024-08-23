import time

import pytest

from internal.infra.adb.adb_function import ADBClient
from internal.infra.pages.general_page import GeneralPage
from internal.infra.pages.photos_page import PhotosPage


@pytest.mark.P0
def test_gallery_app_002():
    """
    步骤：
    1. 打开 Gallery 应用。
    2. 进入 Gallery 应用后，默认页面应为 Photos。
    期望结果：默认页面为 Photos 页面。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    PhotosPage().is_photos_page()


@pytest.mark.P0
def test_gallery_app_004():
    """
    步骤：
    1.打开 Gallery 应用。
    2.在底部区域上滑。
    期望结果：底部区域上滑后，能够正常离开 Gallery 应用。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    time.sleep(2)
    PhotosPage().close_gallery_with_swipe_up()
    GeneralPage().is_launcher_page()


@pytest.mark.P0
def test_gallery_app_005():
    """
    步骤：
    1.打开 Gallery 应用。
    2.在底部区域上滑至 1/3 处停住。
    期望结果：上滑至 1/3 处停住后，能够正常进入"多应用选单"。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    PhotosPage().go_to_recent_app_with_swipe_up()
    GeneralPage().is_recent_app_page()


@pytest.mark.P0
def test_gallery_app_006():
    """
    已經打開過其他應用
    步骤：
    "1.打开 Gallery 应用。
    2.在底部区域左滑。"
    期望结果：底部区域左滑后，能够正常进入前一个应用。
    """
    ADBClient.clear_gallery_cache()
    ADBClient.start_settings()
    ADBClient.stop_settings()

    ADBClient.start_gallery_app()
    PhotosPage().go_to_last_app_with_swipe_left()
    GeneralPage().is_settings_page()
    ADBClient.stop_settings()
