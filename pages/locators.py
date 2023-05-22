from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_i")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_ITEMS_SECTION = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, ".content > #content_inner > p")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'registration_form')
    REGISTRATION_FORM_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_FORM_PWD1 = (By.ID, 'id_registration-password1')
    REGISTRATION_FORM_PWD2 = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form .btn.btn-lg.btn-primary")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".content .price_color")
    PRODUCT_NAME = (By.CLASS_NAME, "content h1")
    ADD_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:first-child strong")
    ADD_MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages > div:last-child strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
