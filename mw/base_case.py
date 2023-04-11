import pytest
from _pytest.fixtures import FixtureRequest

from android_code.pages.base_page import BasePage
from android_code.pages.main_page import MainPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, ui_report):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
