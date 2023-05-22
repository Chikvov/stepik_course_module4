from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented."
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented."
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def add_message_is_correct(self):
        assert self.is_element_present(*ProductPageLocators.ADD_MESSAGE_PRODUCT_NAME), "Message with title is not presented."
        add_message_title = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE_PRODUCT_NAME).text
        actual_title = self.get_product_name()
        assert add_message_title == actual_title, f"Title in message ({add_message_title}) different form product title ({actual_title})."

    def basket_price_message_is_correct(self):
        assert self.is_element_present(*ProductPageLocators.ADD_MESSAGE_PRODUCT_PRICE), "Message with price is not presented."
        basket_price = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE_PRODUCT_PRICE).text
        actual_price = self.get_product_price()
        assert basket_price == actual_price, f"Price in messsage ({basket_price}) is not equal to product price ({actual_price})."

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappeare_succes_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should have dissapeared."
