import allure
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction

from mw.utils import BasePageAndroidLocators

CLICK_RETRY = 3
BASE_TIMEOUT = 5
SEND_KEYS_RETRY = 1


class PageNotLoadedException(Exception):
    pass


class BasePageMobile(object):
    locators = BasePageAndroidLocators()

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.device = self.config['device_os']

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step('Clicking {locator}')
    def click_for_android(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def send_keys_for_android(self, locator, keys_to_send, timeout=None):
        for i in range(SEND_KEYS_RETRY):
            try:
                self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(EC.presence_of_element_located(locator))
                element.send_keys(keys_to_send)
                element.send_keys(Keys.ENTER)
                return
            except StaleElementReferenceException:
                if i == SEND_KEYS_RETRY - 1:
                    raise

    def swipe_up(self, swipetime=200):
        """
        Базовый метод свайпа по вертикали
        Описание работы:
        1. узнаем размер окна телефона
        2. Задаем за X - центр нашего экрана
        3. Указываем координаты откуда и куда делать свайп
        4. TouchAction нажимает на указанные стартовые координаты, немного ждет и передвигает нас из одной точки в другую.
        5. release() наши пальцы с экрана, а perform() выполняет всю эту цепочку команд.
        """
        action = TouchAction(self.driver)
        dimension = self.driver.get_window_size()
        x = int(dimension['width'] / 2)
        start_y = int(dimension['height'] * 0.8)
        end_y = int(dimension['height'] * 0.2)
        action. \
            press(x=x, y=start_y). \
            wait(ms=swipetime). \
            move_to(x=x, y=end_y). \
            release(). \
            perform()

    def swipe_left(self, swipetime=100):
        action = TouchAction(self.driver)
        dimension = self.driver.get_window_size()
        y = int(dimension['height'] * 0.92)
        start_x = int(dimension['width'] * 0.8)
        end_x = int(dimension['width'] * 0.2)
        action. \
            press(x=start_x, y=y). \
            wait(ms=swipetime). \
            move_to(x=end_x, y=y). \
            release(). \
            perform()
