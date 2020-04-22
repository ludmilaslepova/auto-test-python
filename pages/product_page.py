from .base_page import BasePage
from .login_page import LoginPage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def should_be_added_in_cart_succefully(self):
        self.add_item_in_cart()
        self.wait_until_alert_is_present()
        
    def should_be_checked_in_cart(self):
        self.check_book_name_in_cart()
        self.check_book_price()

    def should_be_success_message_after_adding_in_cart(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def success_message_should_disappear_after_adding_in_cart(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message did not disappear"

    def add_item_in_cart(self):
        button_buy = self.browser.find_element(*ProductPageLocators.BUY_BUTTON)
        button_buy.click()

    def wait_until_alert_is_present(self):
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        
    def check_book_name_in_cart(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_check = self.browser.find_element(*ProductPageLocators.BOOK_NAME_CHECK).text
        assert book_name == book_name_check, f"Book name is not the same as in the cart! Expected {book_name}, got {book_name_check}."

    def check_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        book_price_check = self.browser.find_element(*ProductPageLocators.PRICE_CHECK).text
        assert book_price == book_price_check, f"Book price is not the same as in the cart! Expected {book_price}, got {book_price_check}." 
