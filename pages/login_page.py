from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, "No 'login' substring in page url."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        input = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_EMAIL)
        input.send_keys(email)
        input = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PWD1)
        input.send_keys(password)
        input = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PWD2)
        input.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()
