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



