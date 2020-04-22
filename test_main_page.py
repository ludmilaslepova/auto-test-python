import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      
        page.go_to_login_page() 
        page_log = LoginPage(browser, url=browser.current_url)
        page_log.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.skip
def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

@pytest.mark.xfail
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_online_cart_page()
    page_basket = BasketPage(browser, url=browser.current_url)
    page_basket.should_be_empty_cart()

