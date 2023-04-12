import allure
import pytest

from web.pages import MontPage
from web.pages import LoginPage

from web.base_case import BaseCase


class TestMosedo(BaseCase):
    @pytest.mark.UI
    def test_login(self):
        self.login_page.login()
        page = self.login_page
        with allure.step("Логотип после авторизации найден"):
            page.logo_located(timeout=5)

    @pytest.mark.UI
    def test_mont_page(self):
        self.mont_page.open_mont_page()
        page = self.mont_page
        with allure.step("Документооборот на смартфоне"):
            page.mont_generator_located(timeout=5)
