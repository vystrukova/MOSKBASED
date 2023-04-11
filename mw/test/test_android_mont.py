import allure
import pytest
import os
from mw.base_case import BaseCase
from mw.pages import MainPage
from time import sleep


@pytest.mark.AndroidUI
class TestMontAndroid(BaseCase):

    def test_skip(self):
        self.main_page.click_on_skip_button()
        assert self.main_page.find_login_activity()
