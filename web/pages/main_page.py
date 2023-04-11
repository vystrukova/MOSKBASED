import time

from web.pages import BasePage
from web.utils import MainPageLocators
from selenium.webdriver import Chrome


class MainPage(BasePage):
    def __init__(self, browser):
        self.locators = MainPageLocators
        self.browser: Chrome = browser
        super().__init__(browser)

    def is_open(self, timeout):
        locator = self.locators.MAIN_MENU_BLOCK
        for _ in range(timeout):
            if self.is_visible(locator, timeout):
                return True
            time.sleep(0.5)
        return False