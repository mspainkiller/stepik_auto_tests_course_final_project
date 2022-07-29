from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-default[href*='basket']")


class BasketPageLocators:
    BASKET_ITEMS_CONTAINER = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner p")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REG_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_INPUT_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert-success div.alertinner strong")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alert-info div.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")

