import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from web.utils import BasePageLocators


class BasePage(object):
    locators = BasePageLocators()

    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def return_url(self):
        return self.browser.current_url

    def click(self, locator, timeout=2, retries=2):
        """
        Кликает на элемент
        """
        for i in range(retries):
            if i == retries - 1:
                raise TimeoutException
            try:
                WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
                WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator)).click()
                break
            except TimeoutException:
                pass

    def click_visible_element(self, locator, timeout):
        """
        Кликает элемент по локатору
        Возвращает True если успешно кликает
        """
        for _ in range(timeout):
            if self.is_visible(locator, timeout):
                self.browser.find_element(*locator).click()
                return True
            time.sleep(0.5)
        return False

    def get_attribute_value(self, locator, attribute_name, timeout=2):
        """
        Возвращает значение выбранного атрибута у найденного элемента страницы.
        """
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute_name)

    def is_visible(self, locator, timeout):
        """
        Проверяет что элемент visible
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def get_text(self, locator, timeout):
        """
        Берет текст из элемента
        """
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    def get_src(self, locator, timeout):
        """
        Берет src из элемента
        """
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.get_attribute("src")

    def get_href(self, locator, timeout):
        """
        Берет href из элемента
        """
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.get_attribute("href")

    def get_input_value(self, locator, timeout):
        """
        Берет значение из поля ввода
        """
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.get_attribute("value")

    def send_keys(self, locator, text, timeout=2):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def send_enter(self, locator, timeout=2):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        element.send_keys(Keys.ENTER)

    def switch_tab(self, index):
        """
        Меняет вкладку в браузере по индексу
        """
        handles = self.browser.window_handles
        if index >= len(handles):
            raise Exception(f"Invalid tab index {index}")
        self.browser.switch_to.window(handles[index])

    def wait_for_clickable(self, locator, timeout):
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
            return element
        except:
            return None

    def wait_for_visible(self, locator, timeout):
        for _ in range(timeout):
            if self.is_visible(locator, timeout):
                return True
            time.sleep(0.5)
        return False

    def wait_for_all_visible(self, locator, timeout=5):
        """
        Ждет появления всех элементов, соответствующих локатору на странице
        :return: список элементов, если все элементы появились, None в противном случае
        """
        if timeout is None:
            timeout = 5
        for _ in range(timeout):
            elements = self.browser.find_elements(*locator)
            if all([element.is_displayed() for element in elements]):
                return elements
            time.sleep(0.5)
        return None

    def are_all_visible(self, locator):
        """
        Проверяет, что все элементы, соответствующие локатору, видимы на странице
        :return: True, если все элементы видимы, False в противном случае
        """
        elements = self.browser.find_elements(*locator)
        for element in elements:
            if not element.is_displayed():
                return False
        return True

    def mouse_over(self, locator, timeout=1):
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        ActionChains(self.browser).move_to_element(element).perform()

    def click(self, locator, timeout):
        self.mouse_over(locator, timeout)
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)).click()
        return self

    def click_when_loaded(self, locator, timeout_for_click=2, timeout_for_wait=3,
                          retries_spinner=2, retries_no_spinner=4):
        """Кликает на выбранный элемент после того, как со страницы исчезнет спиннер загрузки."""
        if self.page_is_loaded(timeout_for_wait, retries_spinner, retries_no_spinner):
            WebDriverWait(self.browser, timeout_for_click).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.browser, timeout_for_click).until(EC.element_to_be_clickable(locator)).click()
        else:
            raise TimeoutException

    def send_keys(self, locator, text, timeout=5):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.browser, timeout=timeout)

    def is_visible(self, locator, timeout):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def is_attribute_value(self, text, locator, timeout):
        """Проверяет наличие текста в эл-те"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return True
        except:
            return False

    def page_is_loaded(self, timeout, retries_to_appear, retries_to_disappear):
        """Ждет завершения загрузки страницы, отслеживая появление и исчезновение со страницы спиннера загрузки."""
        for i in range(retries_to_appear):
            try:
                WebDriverWait(self.browser, timeout).until(
                    EC.visibility_of_element_located(self.base_locators.SPINNER))
                for j in range(retries_to_disappear):
                    try:
                        WebDriverWait(self.browser, timeout).until(
                            EC.invisibility_of_element_located(self.base_locators.SPINNER))
                        return True
                    except:
                        if j == retries_to_disappear - 1:
                            return False
                        pass
            except:
                if i == retries_to_appear - 1:
                    return True
                pass
