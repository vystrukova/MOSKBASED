import os
from .fixtures import *


class UnsupportedDeviceOs(Exception):
    pass


def pytest_addoption(parser):
    parser.addoption('--device_os', default='android')
    parser.addoption('--appium', default='http://127.0.0.1:4723/wd/hub')


@pytest.fixture(scope='session')
def config(request):
    device_os = request.config.getoption('--device_os')
    appium_url = request.config.getoption('--appium')
    return {'device_os': device_os, 'appium': appium_url}


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))


@pytest.fixture(scope='function')
def test_dir(request):
    test_name = request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    test_dir = os.path.join(request.config.base_test_dir, test_name)
    os.makedirs(test_dir)
    return test_dir