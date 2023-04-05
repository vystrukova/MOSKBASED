import allure
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage


class TestMosedo():
    @pytest.mark.UI
    def test_login(self, browser):
        LoginPage(browser=browser).open()
        page = LoginPage(browser=browser).login()
        with allure.step("Логотип после авторизации найден"):
            page.logo_located(timeout=5)
