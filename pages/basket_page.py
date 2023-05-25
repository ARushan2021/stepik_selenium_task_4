from .locators import ProductPageLocators
from .product_page import ProductPage


class BasketPage(ProductPage):

    def assert_product_message_in_basket(self, exp_name_book):
        product_message_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE_IN_BASKET).text
        assert f'{product_message_in_basket}' == f'{exp_name_book} has been added to your basket.', \
            f'Name book in basket invalid! expected name - {exp_name_book}, actual name - {product_message_in_basket}'

    def assert_price_in_basket(self, exp_price_book):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert price_in_basket == exp_price_book, \
            f'Price in basket invalid! expected price - {exp_price_book}, actual price - {price_in_basket[14:]}'

    def should_not_be_basket_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_BASKET), \
            "Success message is presented, but should not be"