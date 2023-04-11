import os
import shutil
import sys

import allure
import appium
import pytest
from appium import webdriver
from android_code.pages.base_page import BasePage
from android_code import pages

from capability import capability_select


class UnsupportedBrowserType(Exception):
    pass


def pytest_addoption(parser):
    parser.addoption('--os', default='android_code')
    parser.addoption('--appium', default='http://127.0.0.1:4723/wd/hub')


@pytest.fixture(scope='session')
def config(request):
    device_os = request.config.getoption('--os')
    appium = request.config.getoption('--appium')
    return {'device_os': device_os, 'appium': appium}


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))


@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, config=config)


@pytest.fixture
def main_page(driver, config):
    page = get_page(config['device_os'], 'MainPage')
    return page(driver=driver, config=config)


@pytest.fixture(scope='function')
def test_dir(request):
    test_name = request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    test_dir = os.path.join(request.config.base_test_dir, test_name)
    os.makedirs(test_dir)
    return test_dir


def get_page(device, page_class):
    if device == 'android_code':
        page_class += 'ANDROID'
    page = getattr(pages, page_class, None)
    if page is None:
        raise Exception(f'No such page {page_class}')
    return page


def get_driver(device_os, appium_url):
    if device_os == 'android_code':
        desired_caps = capability_select(device_os)
        driver = webdriver.Remote(appium_url, desired_capabilities=desired_caps)
        return driver
    else:
        raise UnsupportedBrowserType(f' Unsupported device_os type {device_os}')


@pytest.fixture(scope='function')
def driver(config):
    device_os = config['device_os']
    appium_url = config['appium']
    browser = get_driver(device_os, appium_url)
    yield browser
    browser.quit()



