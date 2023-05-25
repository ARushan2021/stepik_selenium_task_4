from .base_page import BasePage
from .locators import ProductPageLocators, MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_message_empty_basket(self):
        assert True



