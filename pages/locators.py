from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')

class ProductPageLocators():
    BUY_BUTTON = (By.CSS_SELECTOR, '[value="Add to basket"]')
    BOOK_NAME = (By.TAG_NAME, 'div.col-sm-6.product_main>h1')
    BOOK_NAME_CHECK = (By.TAG_NAME, 'div.alertinner>strong')
    PRICE_CHECK = (By.TAG_NAME, 'div.alertinner>p>strong')
    PRICE = (By.TAG_NAME, 'div.col-sm-6.product_main>p.price_color')