from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO_TEXT = (By.XPATH, "//h1[@class='title']")
    SPINNER = (By.CSS_SELECTOR, "spinner-border")


class LoginPageLocators(BasePageLocators):
    ORGANIZATION_FIELD = (By.XPATH, "//input[@id='organizations']")
    ORGANIZATION_CHOICE = (By.XPATH, "//ul[@id='ui-id-1']//a[text()='Разработчики Автотест']")

    LOGIN_FIELD = (By.XPATH, "//input[@id='logins']")
    LOGIN_CHOICE = (By.XPATH, "//ul[@id='ui-id-2']//a[text()='Пользователь МОНТ']")

    PASSWORD_FIELD = (By.XPATH, "//input[@id='password_input']")

    LOGIN_BUTTON = (By.XPATH, "//input[@class='btn_enter']")

    LOGO_LOCATED = (By.XPATH, "//i[@class='mont-promotion-link__icon']")


class MainPageLocators(BasePageLocators):
    MAIN_MENU_BLOCK = (By.XPATH, "//div[@class='s-menu__block']")


class MontPageLocators(BasePageLocators):
    #MONT_PAGE = (By.XPATH, "//i[@class='mont-promotion-link__icon']")
    MONT_PAGE = (By.XPATH, "//span[text()='Документооборот ']")
    MONT_GENERATOR = (By.XPATH, "//div[@class='login-and-password-generator guide__login-and-password-generator']")
    MONT_GENERATE_BUTTON = (By.XPATH, "//button[contains(text(), 'Сгенерировать')]")
    MONT_TIMER = (By.XPATH, "//div[@class='timer']")
    MONT_DATA = (By.XPATH, "//div[@class='digits']//span")

    MONT_CODE_BLOCK = (By.XPATH, "//div[@class='confirmation-code-popup__input-wrapper']")
    MONT_CODE_INPUT = (By.XPATH, "//input[@class='confirmation-code-popup__input']")

    MONT_CONFIRMATION_FIRST = (By.XPATH, "//input[@class='confirmation-code-popup__input'][1]")
    MONT_CONFIRMATION_SECOND = (By.XPATH, "//input[@class='confirmation-code-popup__input'][2]")
    MONT_CONFIRMATION_THIRD = (By.XPATH, "//input[@class='confirmation-code-popup__input'][3]")

    MONT_LOGINED = (By.XPATH, "//div[@class='successful-login__header']")

