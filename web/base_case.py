import pytest
from _pytest.fixtures import FixtureRequest

from web.pages.base_page import BasePage
from web.pages.login_page import LoginPage
from web.pages.main_page import MainPage
from web.pages.mont_page import MontPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser, request: FixtureRequest):
        self.browser = browser

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.mont_page: MontPage = request.getfixturevalue('mont_page')

