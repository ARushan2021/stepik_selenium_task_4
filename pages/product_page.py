from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators


class ProductPage(BasePage):

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should to be"

    def main_name_book(self):
        name_book = self.browser.find_element(*MainPageLocators.NAME_BOOK).text
        return name_book

    def main_price_book(self):
        price_book = self.browser.find_element(*MainPageLocators.PRICE_BOOK).text
        return price_book