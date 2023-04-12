import os

from selenium.webdriver import Chrome

from .login_page import LoginPage
from .base_page import BasePage
from web.utils import MontPageLocators
from web.utils import Info


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

    def mont_data_button_located(self, timeout):
        locator = self.locators.MONT_GENERATE_BUTTON
        return self.wait_for_visible(locator, timeout)

    def click_mont_data(self, timeout):
        locator = self.locators.MONT_GENERATE_BUTTON
        if self.mont_data_button_located(timeout=1):
            self.click_visible_element(locator, timeout)

    def mont_timer_located(self, timeout):
        locator = self.locators.MONT_TIMER
        return self.wait_for_visible(locator, timeout)

    def get_mont_data_values(self, timeout=None):
        mont_data_values = []
        mont_data_elements = self.wait_for_all_visible(self.locators.MONT_DATA, timeout)
        for mont_data_element in mont_data_elements:
            mont_data_values.append(mont_data_element.text)
        return mont_data_values

    def split_mont_data_values(self, timeout=None):
        # Получаем список значений элементов
        mont_data_values = self.get_mont_data_values(timeout=timeout)
        # Получаем длину списка
        values_count = len(mont_data_values)
        # Если число элементов нечетное, добавляем пустую строку в конец списка
        if values_count % 2 == 1:
            mont_data_values.append('')
            values_count += 1
        # Разделяем список на две части
        half_count = values_count // 2
        first_half = "".join(mont_data_values[:len(mont_data_values) // 2]).replace(" ", "")
        second_half = "".join(mont_data_values[len(mont_data_values) // 2:]).replace(" ", "")
        # self.write_to_file("mont_data", "first_half.txt", first_half)
        # self.write_to_file("mont_data", "second_half.txt", second_half)
        # Возвращаем две части в виде кортежа
        return first_half, second_half

    def write_to_file(self, folder_name, file_name, data):
        os.makedirs(folder_name, exist_ok=True)
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as f:
            f.write(data)
        print(f"Data written to {file_path} successfully.")

    """
    Документооборот на смартфоне
    """
    def open_mont_page(self):
        LoginPage(browser=self.browser).login()
        self.mont_page_located(timeout=1)
        self.click_mont_page(timeout=1)
        self.mont_generator_located(timeout=1)
        self.mont_data_button_located(timeout=1)
        self.click_mont_data(timeout=1)
        self.mont_timer_located(timeout=1)
        self.get_mont_data_values(timeout=1)
        self.split_mont_data_values(timeout=1)

        return MontPage(browser=self.browser)

    def mont_login_password(self):
        LoginPage(browser=self.browser).login()
        self.mont_page_located(timeout=1)
        self.click_mont_page(timeout=1)
        self.mont_generator_located(timeout=1)
        self.mont_data_button_located(timeout=1)
        self.click_mont_data(timeout=1)
        self.mont_timer_located(timeout=1)
        self.get_mont_data_values(timeout=1)

        return MontPage(browser=self.browser)
