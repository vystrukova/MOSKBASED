import allure
import pytest
from mw.base_case import BaseCase


@pytest.mark.AndroidUI
class TestMontAndroid(BaseCase):

    def test_skip(self):
        self.main_page.click_on_skip_button()
        login_button_text = self.main_page.check_login_text()
        assert 'Войти' in login_button_text
