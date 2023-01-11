import time
from selenium.webdriver import Chrome
from ui.locators import BasePageLocators
from ui.locators import LoginPageLocators
from ui.locators import MainPageLocators
from ui.base_page import BasePage
import ui.main_page
import info


class LoginPage(BasePage):
    #url = "https://mosedo.release133.sedmsk81/"
    #locators = LoginPageLocators

    def __init__(self, browser):
        self.locators = LoginPageLocators
        self.browser: Chrome = browser
        self.url = "https://mosedo.release133.sedmsk81/"
        super().__init__(browser)

    """Открывает страницу в браузере"""
    def open(self):
        self.browser.get(self.url)
        return self

    """Проверяем что страница открыта"""
    def page_is_open(self, timeout):
        locator = self.locators.LOGIN_BUTTON
        for _ in range(timeout):
            if self.is_visible(locator, timeout):
                return True
            time.sleep(0.5)
        return False

    """Авторизация"""
    def login(self, organization=info.organization, login=info.login, password=info.password):
        self.browser.get(self.url)
        self.send_keys(self.locators.ORGANIZATION_FIELD, organization)
        #self.click(self.locators.ORGANIZATION_CHOICE, timeout=1)
        self.click_when_loaded(self.locators.ORGANIZATION_CHOICE, timeout_for_click=2, timeout_for_wait=3, retries_spinner=2, retries_no_spinner=1)
        #self.key_down()
        self.send_keys(self.locators.LOGIN_FIELD, login)
        self.click_when_loaded(self.locators.LOGIN_CHOICE, timeout_for_click=2, timeout_for_wait=3, retries_spinner=2, retries_no_spinner=1)
        #self.click(self.locators.LOGIN_CHOICE, timeout=1)
        #self.key_down()
        self.send_keys(self.locators.PASSWORD_FIELD, password)
        self.click(self.locators.LOGIN_BUTTON, timeout=1)
        self.page_is_loaded(4, 1, 4)
        return ui.main_page.MainPage(browser=self.browser)


