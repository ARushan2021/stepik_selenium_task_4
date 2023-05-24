import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}'
    page = ProductPage(browser, link)
    page.open()
    main_name_book = page.main_name_book()
    main_price_book = page.main_price_book()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.assert_product_message_in_basket(main_name_book)
    page.assert_price_in_basket(main_price_book)
    page.clear_basket()

# pytest -s test_product_page.py
