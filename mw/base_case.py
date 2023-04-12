import pytest
from _pytest.fixtures import FixtureRequest

from mw.pages.base_page_mobile import BasePageMobile
from mw.pages.main_page_mobile import MainPageMobile

from web.pages.base_page import BasePage
from web.pages.main_page import MainPage
from web.pages.login_page import LoginPage
from web.pages.mont_page import MontPage


class BaseCaseMobile:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, browser, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.browser = browser

        self.base_page_mobile: BasePageMobile = request.getfixturevalue('base_page_mobile')
        self.main_page_mobile: MainPageMobile = request.getfixturevalue('main_page_mobile')

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.mont_page: MontPage = request.getfixturevalue('mont_page')
