from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_OUT = (By.CSS_SELECTOR, "#logout_link")
    VIEW_BASKET = (By.CSS_SELECTOR, "span>a[class='btn btn-default']")


class MainPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form>button")
    NAME_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    PRICE_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main>p.price_color")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "#register_form>button")


class ProductPageLocators:
    PRODUCT_MESSAGE_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, 'div[class="alertinner "]>p>strong')
    QUANTITY_PRODUCTS = (By.CSS_SELECTOR, "#id_form-0-quantity")
    BUTTON_UPDATE = (By.CSS_SELECTOR, "div>span> button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div>strong")


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner>p')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '[class="col-sm-6 h3"]')

