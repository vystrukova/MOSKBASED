import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.login_page import LoginPage
from ui.main_page import MainPage


class TestMosedo():
    @pytest.mark.UI
    def test_open(self, browser):
        page = LoginPage(browser=browser).open()
        assert page.page_is_open(timeout=5) is True

    @pytest.mark.UI
    def test_login(self, browser):
        LoginPage(browser=browser).open()
        page = LoginPage(browser=browser).login()
        assert page.is_open(timeout=5) is True