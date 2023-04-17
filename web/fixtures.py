import pytest
from selenium import webdriver

from web.pages.base_page import BasePage
from web.pages.login_page import LoginPage
from web.pages.main_page import MainPage
from web.pages.mont_page import MontPage
from web.pages.rezolution_page import RezolutionPage
from web import pages


@pytest.fixture
def base_page(browser):
    return BasePage(browser=browser)


@pytest.fixture
def login_page(browser):
    return LoginPage(browser=browser)


@pytest.fixture
def main_page(browser):
    return MainPage(browser=browser)


@pytest.fixture
def mont_page(browser):
    return MontPage(browser=browser)


@pytest.fixture
def rezolution_page(browser):
    return RezolutionPage(browser=browser)
