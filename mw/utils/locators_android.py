from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy


class BasePageAndroidLocators:
    pass


class MainPageAndroidLocators(BasePageAndroidLocators):
    SKIP_BUTTON = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.Button")
    LOGIN_BUTTON = (AppiumBy.ID, "ru.docsystems.mont:id/login_fragment_login_button")
