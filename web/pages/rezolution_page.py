import os

from selenium.webdriver import Chrome

from .login_page import LoginPage
from .base_page import BasePage
from web.utils import RezolutionPageLocators
from web.utils import Info


class RezolutionPage(BasePage):
    def __init__(self, browser):
        self.locators = RezolutionPageLocators
        self.browser: Chrome = browser
        self.url = Info.base_url
        super().__init__(browser)

    def open(self):
        self.browser.get(self.url)
        return self

    def document_block_located(self, timeout):
        locator = self.locators.MENU_CATEGORY_0
        return self.wait_for_visible(locator, timeout)

    def click_category_all(self, timeout):
        locator = self.locators.BUTTON_FULL_DOCS
        if self.document_block_located(timeout=1):
            self.click_visible_element(locator, timeout)

    def click_new_document(self, timeout):
        locator = self.locators.BUTTON_NEW_DOCUMENT
        if self.document_block_located(timeout=1):
            self.click_visible_element(locator, timeout)

    def rkd_block_located(self, timeout):
        locator = self.locators.RKD_BLOCK
        return self.wait_for_visible(locator, timeout)

    def attach_file_to_doc(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                 '../../data/test.docx')
                                    ),
        locator = self.locators.FILE_INPUT
        self.attach_file(locator, file_path)

    """
    Создание документа
    """

    def create_document(self):
        LoginPage(browser=self.browser).login()
        self.document_block_located(timeout=1)
        self.click_category_all(timeout=1)
        self.click_new_document(timeout=1)

        return RezolutionPage(browser=self.browser)
