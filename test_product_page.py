import pytest
from pages.base_page import BasePage
from pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page_prod = ProductPage(browser, link)
    page_prod.open()
    page_prod.should_be_added_in_cart_succefully()
    page_prod.solve_quiz_and_get_code()
    page_prod.should_be_checked_in_cart()

