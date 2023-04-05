import allure
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage


class TestMosedo():
    @pytest.mark.UI
    def test_login(self, browser):
        page = LoginPage(browser=browser).open()
        page.main_page_is_open(timeout=1)
        with allure.step("Поле выбора организации найдено"):
            page.organization_field_located(timeout=1)
        page.send_organization()
        page.click_organization(timeout=1)
        with allure.step("Поле ввода пользователя найдено"):
            page.login_field_located(timeout=1)
        page.send_login()
        page.click_login(timeout=1)
        with allure.step("Поле ввода пароля найдено"):
            page.password_field_located(timeout=1)
        page.send_password()
        page.click_login_button(timeout=5)
        with allure.step("Логотип после авторизации найден"):
            page.logo_located(timeout=5)