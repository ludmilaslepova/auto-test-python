from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.XPATH, '//div[contains(@class, "basket-mini")]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, '[name="registration-password2"]')

class ProductPageLocators():
    BUY_BUTTON = (By.CSS_SELECTOR, '[value="Add to basket"]')
    BOOK_NAME = (By.TAG_NAME, 'div.col-sm-6.product_main>h1')
    BOOK_NAME_CHECK = (By.TAG_NAME, 'div.alertinner>strong')
    PRICE_CHECK = (By.TAG_NAME, 'div.alertinner>p>strong')
    PRICE = (By.TAG_NAME, 'div.col-sm-6.product_main>p.price_color')
    SUCCESS_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[1]/div[1]')

class BascketPageLocators():
    INFO_MESSAGE_EMPTY = (By.XPATH, '//div[@class = "content"]//div[@id = "content_inner"]/p[contains(text(), "basket is empty")]')
    CART_ITEM = (By.XPATH, '//div[@class="basket-items"]')

