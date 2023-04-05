import time
from selenium.webdriver import Chrome
from locators import LoginPageLocators
from base_page import BasePage
import info


class LoginPage(BasePage):

    def __init__(self, browser):
        self.locators = LoginPageLocators
        self.browser: Chrome = browser
        self.url = info.base_url
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

    def send_organization(self, login_text=info.organization):
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

    def send_login(self, login_text=info.login):
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

    def send_password(self, password_text=info.password_api):
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


