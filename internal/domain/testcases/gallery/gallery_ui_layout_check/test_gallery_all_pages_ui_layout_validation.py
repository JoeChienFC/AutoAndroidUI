import time

import pytest

from internal.infra.adb.adb_function import ADBClient
from internal.infra.pages.general_page import GeneralPage
from internal.infra.pages.photos_page import PhotosPage
from internal.infra.validators.Image_validators import ImageValidator


@pytest.mark.SSS
def test_ref_page_catch():
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ADBClient.ref_screenshot("PhotosPage_NoPhotos")
    PhotosPage().btn_more_options_click()
    ADBClient.ref_screenshot("SettingsPopover")


@pytest.mark.S
def test_photos_page_no_photos():
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    ImageValidator().validate(ADBClient.screenshot("PhotosPage_NoPhotos"))


@pytest.mark.S
def test_settings_popover():
    ADBClient.clear_gallery_cache()
    ADBClient.start_gallery_app()
    PhotosPage().btn_more_options_click()
    ImageValidator().validate(ADBClient.screenshot("SettingsPopover"))
