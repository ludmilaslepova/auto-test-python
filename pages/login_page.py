from .base_page import BasePage
from .locators import LoginPageLocators

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url==link, "Link is not valid!"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Log in button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"

    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        user_email.send_keys(email)
        user_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        user_password1.send_keys(password)
        user_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        user_password2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()