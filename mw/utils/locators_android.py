from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy


class BasePageAndroidLocators:
    pass


class MainPageAndroidLocators(BasePageAndroidLocators):
    SKIP_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@text='Пропустить']")
    LOGIN_BUTTON = (AppiumBy.ID, "ru.docsystems.mont:id/login_fragment_login_button")
    LOGIN_FIELD = (AppiumBy.ID, "ru.docsystems.mont:id/login_fragment_login_field")
    PASSWORD_FIELD = (AppiumBy.ID, "ru.docsystems.mont:id/login_fragment_password_field")

    FIRST_SYMBOL = (AppiumBy.ID, "ru.docsystems.mont:id/login_verify_fragment_first_code")
    SECOND_SYMBOL = (AppiumBy.ID, "ru.docsystems.mont:id/login_verify_fragment_second_code")
    THIRD_SYMBOL = (AppiumBy.ID, "ru.docsystems.mont:id/login_verify_fragment_third_code")

    ZERO_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@text='0']")
    BUTTON_ONLY_CODE = (AppiumBy.ID, "android:id/button2")
    # BUTTON_ONLY_CODE = (AppiumBy.XPATH, "//android.widget.Button[@text='ИСПОЛЬЗОВАТЬ ТОЛЬКО КОД-ПАРОЛЬ']")


    MY_DOCUMENTS = (AppiumBy.ID, "ru.docsystems.mont:id/tabbar_documents")
