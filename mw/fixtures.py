import pytest
from appium import webdriver
from mw.pages.base_page import BasePage
from mw import pages

from .capability import capability_select


class UnsupportedDeviceOs(Exception):
    pass


@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, config=config)


@pytest.fixture
def main_page(driver, config):
    page = get_page(config['device_os'], 'MainPage')
    return page(driver=driver, config=config)


def get_page(device_os, page_class):
    if device_os == 'android':
        page_class += 'Android'
    else:
        raise UnsupportedDeviceOs(f' Unsupported device_os type {device_os}')
    page = getattr(pages, page_class, None)
    if page is None:
        raise Exception(f'No such page {page_class}')
    return page


def get_driver(device_os, appium_url):
    if device_os == 'android':
        desired_caps = capability_select(device_os)
        driver = webdriver.Remote(appium_url, desired_capabilities=desired_caps)
        return driver
    else:
        raise UnsupportedDeviceOs(f' Unsupported device_os type {device_os}')


@pytest.fixture(scope='function')
def driver(config):
    device_os = config['device_os']
    appium_url = config['appium']
    browser = get_driver(device_os, appium_url)
    yield browser
    browser.quit()