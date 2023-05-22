from .base_page import BasePage
from .locators import ProductPageLocators


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
