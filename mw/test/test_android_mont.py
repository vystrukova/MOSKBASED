import allure
import pytest
from mw.base_case import BaseCaseMobile
from web.base_case import BaseCase


@pytest.mark.AndroidUI
class TestMontAndroid(BaseCaseMobile):

    def test_skip(self):
        self.mont_page.open_mont_page()
        page = self.mont_page
        with allure.step("Документооборот на смартфоне"):
            page.mont_generator_located(timeout=5)
        first_half, second_half = self.mont_page.split_mont_data_values(timeout=5)

        self.main_page_mobile.click_on_skip_button()
        login_button_text = self.main_page_mobile.check_login_text()
        with allure.step("Нажимаем кнопку Пропустить"):
            assert 'Войти' in login_button_text

        with allure.step("Вводим логин и пароль"):
            self.main_page_mobile.send_keys_login(first_half)
            self.main_page_mobile.send_keys_password(second_half)

        with allure.step("Нажимаем на кнопку Войти"):
            self.main_page_mobile.click_login_button()


