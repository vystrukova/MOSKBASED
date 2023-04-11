import allure
import pytest

from web.pages import MontPage
from web.pages import LoginPage


class TestMosedo():
    @pytest.mark.UI
    @pytest.mark.skip
    def test_login(self, browser):
        LoginPage(browser=browser).open()
        page = LoginPage(browser=browser).login()
        with allure.step("Логотип после авторизации найден"):
            page.logo_located(timeout=5)

    @pytest.mark.UI
    def test_mont_page(self, browser):
        MontPage(browser=browser).open()
        page = MontPage(browser=browser).open_mont_page()
        with allure.step("Документооборот на смартфоне"):
            page.mont_generator_located(timeout=5)
