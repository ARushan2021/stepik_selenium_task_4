from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form>button")
    NAME_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    PRICE_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main>p.price_color")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_MESSAGE_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>div")
    PRICE_IN_BASKET = (By.CSS_SELECTOR,
                       '#messages >div.alert.alert-safe.alert-noicon.alert-info.fade.in>div>p:nth-child(1)>strong')
    VIEW_BASKET = (By.CSS_SELECTOR, "#default>header>div.page_inner>div>div.basket-mini.pull-right.hidden-xs>span>a")
    QUANTITY_PRODUCTS = (By.CSS_SELECTOR, "#id_form-0-quantity")
    BUTTON_UPDATE = (By.CSS_SELECTOR, "div>span> button")





