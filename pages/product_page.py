from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        basket_link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        basket_link.click()

    def main_name_book(self):
        name_book = self.browser.find_element(*MainPageLocators.NAME_BOOK).text
        return name_book

    def main_price_book(self):
        price_book = self.browser.find_element(*MainPageLocators.PRICE_BOOK).text
        return price_book

    def assert_product_message_in_basket(self, exp_name_book):
        product_message_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE_IN_BASKET).text
        assert f'{product_message_in_basket}' == f'{exp_name_book} has been added to your basket.', \
            f'Name book in basket invalid! expected name - {exp_name_book}, actual name - {product_message_in_basket}'

    def assert_price_in_basket(self, exp_price_book):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert price_in_basket == exp_price_book, \
            f'Price in basket invalid! expected price - {exp_price_book}, actual price - {price_in_basket[14:]}'

