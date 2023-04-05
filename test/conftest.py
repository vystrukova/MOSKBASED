import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

supported_browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome(chrome_options=options, service=Service(ChromeDriverManager().install()))

    # browser.add_argument('ignore-certificate-errors')
    browser.maximize_window()
    yield browser
    browser.quit()
