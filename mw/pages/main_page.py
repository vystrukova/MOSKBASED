from .base_page import BasePage
from mw.utils import MainPageANDROIDLocators
import allure


class MainPage(BasePage):

    def click_on_skip_button(self):
        pass

    def find_login_activity(self):
        pass


class MainPageANDROID(MainPage):
    locators = MainPageANDROIDLocators()

    @allure.step("Clicking on skip button")
    def click_on_skip_button(self):
        self.click_for_android(self.locators.SKIP_BUTTON)

    @allure.step("Looking for main activity")
    def find_login_activity(self):
        self.find(self.locators.LOGIN_ACTIVITY)
