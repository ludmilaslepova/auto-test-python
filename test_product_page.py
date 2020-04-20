import pytest
from pages.base_page import BasePage
from pages.product_page import ProductPage

@pytest.mark.parametrize('offer', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6", 
                                pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"])

def test_guest_can_go_to_login_page(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{offer}"
    page_prod = ProductPage(browser, link)
    page_prod.open()
    page_prod.should_be_added_in_cart_succefully()
    page_prod.solve_quiz_and_get_code()
    page_prod.should_be_checked_in_cart()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page_prod = ProductPage(browser, link)
    page_prod.open()
    page_prod.add_item_in_cart()
    page_prod.should_be_success_message_after_adding_in_cart()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page_prod = ProductPage(browser, link)
    page_prod.open()
    page_prod.should_be_success_message_after_adding_in_cart()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page_prod = ProductPage(browser, link)
    page_prod.open()
    page_prod.add_item_in_cart()
    page_prod.success_message_should_disappear_after_adding_in_cart()