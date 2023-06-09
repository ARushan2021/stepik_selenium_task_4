from datetime import datetime

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, login_out):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        self.page = LoginPage(browser, link)
        self.page.open()
        timestamp = datetime.timestamp(datetime.now())
        self.page.register_new_user(f'ivan@ivan{timestamp}.ru', f"QWErty{timestamp}")
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        self.page = ProductPage(browser, link)
        self.page.open()
        main_name_book = self.page.main_name_book()
        main_price_book = self.page.main_price_book()
        self.page.add_to_basket()
        self.page.assert_product_message_in_basket(main_name_book)
        self.page.assert_price_in_basket(main_price_book)

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, clear_basket):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    main_name_book = page.main_name_book()
    main_price_book = page.main_price_book()
    page.add_to_basket()
    page.assert_product_message_in_basket(main_name_book)
    page.assert_price_in_basket(main_price_book)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.open_basket()
    page.should_not_be_product_in_basket()
    page.should_be_message_basket_is_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, clear_basket):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = BasketPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser, clear_basket):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_is_disappeared()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.open_basket()
    page.should_not_be_product_in_basket()
    page.should_be_message_basket_is_empty()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
