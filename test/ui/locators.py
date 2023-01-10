from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO_TEXT = (By.XPATH, "//h1[@class='title']")
    SPINNER = (By.CSS_SELECTOR, "spinner-border")


class LoginPageLocators(BasePageLocators):
    ORGANIZATION_FIELD = (By.XPATH, "//input[@id='organizations']")
    ORGANIZATION_CHOICE = (By.XPATH, "//a[@id='ui-id-5']")

    LOGIN_FIELD = (By.XPATH, "//input[@id='logins']")
    LOGIN_CHOICE = (By.XPATH, "//a[@id='ui-id-183']")

    PASSWORD_FIELD = (By.XPATH, "//input[@id='password_input']")

    LOGIN_BUTTON = (By.XPATH, "//input[@class='btn_enter']")


class MainPageLocators(BasePageLocators):
    MAIN_MENU_BLOCK = (By.XPATH, "//div[@class='s-menu__block']")