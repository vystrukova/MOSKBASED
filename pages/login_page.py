from selenium.webdriver import Chrome

from utils.locators import LoginPageLocators
from .base_page import BasePage
from utils.info import Info


class LoginPage(BasePage):

    def __init__(self, browser):
        self.locators = LoginPageLocators
        self.browser: Chrome = browser
        self.url = Info.base_url
        super().__init__(browser)

    def open(self):
        self.browser.get(self.url)
        return self

    def main_page_is_open(self, timeout):
        locator = self.locators.LOGO_TEXT
        return self.wait_for_visible(locator, timeout)

    def organization_field_located(self, timeout):
        locator = self.locators.ORGANIZATION_FIELD
        return self.wait_for_visible(locator, timeout)

    def send_organization(self, login_text=Info.organization):
        locator = self.locators.ORGANIZATION_FIELD
        if self.organization_field_located(timeout=1):
            self.send_keys(locator, login_text)
            return True
        return False

    def click_organization(self, timeout):
        locator = self.locators.ORGANIZATION_CHOICE
        return self.click_visible_element(locator, timeout)

    def login_field_located(self, timeout):
        locator = self.locators.LOGIN_FIELD
        return self.wait_for_visible(locator, timeout)

    def send_login(self, login_text=Info.login):
        locator = self.locators.LOGIN_FIELD
        if self.login_field_located(timeout=1):
            self.send_keys(locator, login_text)
            return True
        return False

    def click_login(self, timeout):
        locator = self.locators.LOGIN_CHOICE
        return self.click_visible_element(locator, timeout)

    def password_field_located(self, timeout):
        locator = self.locators.PASSWORD_FIELD
        return self.wait_for_visible(locator, timeout)

    def send_password(self, password_text=Info.password):
        locator = self.locators.PASSWORD_FIELD
        if self.password_field_located(timeout=1):
            self.send_keys(locator, password_text)
            return True
        return False

    def click_login_button(self, timeout):
        locator = self.locators.LOGIN_BUTTON
        return self.click_visible_element(locator, timeout)

    def logo_located(self, timeout):
        locator = self.locators.LOGO_LOCATED
        return self.wait_for_visible(locator, timeout)

    """
    Авторизация
    """
    def login(self):
        self.browser.get(self.url)
        self.main_page_is_open(timeout=1)
        self.organization_field_located(timeout=1)
        self.send_organization()
        self.click_organization(timeout=1)
        self.login_field_located(timeout=1)
        self.send_login()
        self.click_login(timeout=1)
        self.password_field_located(timeout=1)
        self.send_password()
        self.click_login_button(timeout=1)
        self.logo_located(timeout=1)
        return LoginPage(browser=self.browser)



