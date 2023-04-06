from selenium.webdriver import Chrome

from .login_page import LoginPage
from .base_page import BasePage
from utils.locators import MontPageLocators
from utils.info import Info


class MontPage(BasePage):
    def __init__(self, browser):
        self.locators = MontPageLocators
        self.browser: Chrome = browser
        self.url = Info.base_url
        super().__init__(browser)

    def open(self):
        self.browser.get(self.url)
        return self

    def mont_page_located(self, timeout):
        locator = self.locators.MONT_PAGE
        return self.wait_for_visible(locator, timeout)

    def click_mont_page(self, timeout):
        locator = self.locators.MONT_PAGE
        if self.mont_page_located(timeout=1):
            self.click_visible_element(locator, timeout)

    def mont_generator_located(self, timeout):
        locator = self.locators.MONT_GENERATOR
        return self.wait_for_visible(locator, timeout)

    """
    Документооборот на смартфоне
    """
    def open_mont_page(self):
        LoginPage(browser=self.browser).login()
        self.mont_page_located(timeout=1)
        self.click_mont_page(timeout=1)
        self.mont_generator_located(timeout=1)
        return MontPage(browser=self.browser)
