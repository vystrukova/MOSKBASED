import allure
import pytest
from mw.base_case import BaseCaseMobile
from web.base_case import BaseCase


class AutorizationMontAndroid(BaseCaseMobile):

    def autorization_mont_android(self):
        self.mont_page.open_mont_page()
        page = self.mont_page
        page.mont_generator_located(timeout=5)
        first_half, second_half = self.mont_page.split_mont_data_values(timeout=5)

        self.main_page_mobile.click_on_skip_button()
        login_button_text = self.main_page_mobile.check_login_text()
        assert 'Войти' in login_button_text

        self.main_page_mobile.send_keys_login(first_half)
        self.main_page_mobile.send_keys_password(second_half)

        self.main_page_mobile.click_login_button()

        first_symbol, second_symbol, third_symbol = self.main_page_mobile.get_confirmation_code()

        self.mont_page.wait_for_visible(self.mont_page.locators.MONT_CONFIRMATION_FIRST, timeout=1)
        self.mont_page.wait_for_visible(self.mont_page.locators.MONT_CONFIRMATION_SECOND, timeout=1)
        self.mont_page.wait_for_visible(self.mont_page.locators.MONT_CONFIRMATION_THIRD, timeout=1)

        self.mont_page.send_keys(self.mont_page.locators.MONT_CONFIRMATION_FIRST, first_symbol)
        self.mont_page.send_keys(self.mont_page.locators.MONT_CONFIRMATION_SECOND, second_symbol)
        self.mont_page.send_keys(self.mont_page.locators.MONT_CONFIRMATION_THIRD, third_symbol)

        assert self.mont_page.mont_is_logined(timeout=3)

        self.main_page_mobile.code_password()
        # self.main_page_mobile.code_password_another()
        self.main_page_mobile.code_password()
        # self.main_page_mobile.code_password_another()
        self.main_page_mobile.check_documents_tab()