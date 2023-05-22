from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'registration_form')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".content .price_color")
    PRODUCT_NAME = (By.CLASS_NAME, "content h1")
    ADD_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:first-child strong")
    ADD_MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages > div:last-child strong")
