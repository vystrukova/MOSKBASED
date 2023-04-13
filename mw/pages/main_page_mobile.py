from .base_page_mobile import BasePageMobile
from mw.utils import MainPageAndroidLocators
import allure


class MainPageMobile(BasePageMobile):

    def click_on_skip_button(self):
        pass

    def check_login_text(self):
        pass

    def send_keys_login(self):
        pass

    def send_keys_password(self):
        pass

    def click_login_button(self):
        pass

    def get_confirmation_code(self):
        pass


class MainPageMobileAndroid(MainPageMobile):
    locators = MainPageAndroidLocators()

    @allure.step("Нажимаем на кнопку Пропустить")
    def click_on_skip_button(self):
        self.click_for_android(self.locators.SKIP_BUTTON)

    @allure.step("Ищем надпись Войти на кнопке")
    def check_login_text(self):
        mont_info = self.find(self.locators.LOGIN_BUTTON)
        return mont_info.text

    @allure.step("Вводим логин")
    def send_keys_login(self, login_text):
        login_field = self.find(self.locators.LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(login_text)

    @allure.step("Вводим пароль")
    def send_keys_password(self, password_text):
        password_field = self.find(self.locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password_text)

    @allure.step("Нажимаем на кнопку Войти")
    def click_login_button(self):
        self.click_for_android(self.locators.LOGIN_BUTTON)

    @allure.step("Получаем код подтверждения")
    def get_confirmation_code(self):
        first_symbol = self.get_text_for_android(self.locators.FIRST_SYMBOL)
        second_symbol = self.get_text_for_android(self.locators.SECOND_SYMBOL)
        third_symbol = self.get_text_for_android(self.locators.THIRD_SYMBOL)
        return first_symbol, second_symbol, third_symbol
