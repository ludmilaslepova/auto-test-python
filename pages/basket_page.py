from .base_page import BasePage
from .locators import BascketPageLocators

class BasketPage(BasePage):

    def should_be_empty_cart(self):
        self.should_be_message_about_emty_cart()
        self.should_be_no_items_in_cart()

    def should_be_message_about_emty_cart(self):
        assert self.is_element_present(*BascketPageLocators.INFO_MESSAGE_EMPTY), "There is no message about emptiness!"

    def should_be_no_items_in_cart(self):
        assert self.is_element_present(*BascketPageLocators.CART_ITEM), "There is an empty cart!"

