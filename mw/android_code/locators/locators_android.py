from appium.webdriver.common.mobileby import MobileBy


class BasePageANDROIDLocators:
    pass


class MainPageANDROIDLocators(BasePageANDROIDLocators):
    SKIP_BUTTON = (MobileBy.XPATH, "//*[contains(@id,'00000000-0000-0043-ffff-ffff0000000a')]")
    LOGIN_ACTIVITY = (MobileBy.ID, 'ru.docsystems.mont:id/login_fragment_main_layout')
