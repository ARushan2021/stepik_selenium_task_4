from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators
from .product_page import ProductPage


class BasketPage(ProductPage):

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_be_message_basket_is_empty(self):
        self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET)
