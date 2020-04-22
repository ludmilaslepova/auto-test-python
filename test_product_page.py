import pytest
import time
from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link_reg = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page_reg = LoginPage(browser, link_reg)
        page_reg.open()
        self.usr_email = str(time.time()) + "@fakemail.org"
        self.usr_password = str(time.time()) + "1234"
        page_reg.register_new_user(email=self.usr_email, password=self.usr_password)
        page_reg.should_be_authorized_user()       

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page_prod = ProductPage(browser, link)
        page_prod.open()
        page_prod.should_be_success_message_after_adding_in_cart()
    
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page_prod = ProductPage(browser, link)
        page_prod.open()
        page_prod.add_item_in_cart()


@pytest.mark.parametrize('offer', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6", 
                                pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"])
@pytest.mark.skip
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
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_online_cart_page()
    page_basket = BasketPage(browser, url=browser.current_url)
    page_basket.should_be_empty_cart()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page_prod = ProductPage(browser, link)
    page_prod.open()
    page_prod.add_item_in_cart()
    page_prod.success_message_should_disappear_after_adding_in_cart()