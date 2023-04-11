from .base_page import BasePage
from mw.utils import MainPageAndroidLocators
import allure


class MainPage(BasePage):

    def click_on_skip_button(self):
        pass

    def check_login_text(self):
        pass


class MainPageAndroid(MainPage):
    locators = MainPageAndroidLocators()

    @allure.step("Нажимаем на кнопку Пропустить")
    def click_on_skip_button(self):
        self.click_for_android(self.locators.SKIP_BUTTON)

    @allure.step("Ищем надпись Войти на кнопке")
    def check_login_text(self):
        mont_info = self.find(self.locators.LOGIN_BUTTON)
        return mont_info.text
