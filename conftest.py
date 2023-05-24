import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.chrome.options import Options

from .pages.locators import ProductPageLocators


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language: en, fr, ...")
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="session")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")

        options_chrome = Options()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options_firefox = FirefoxProfile()
        options_firefox.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def clear_basket(browser):
    yield
    browser.find_element(*ProductPageLocators.VIEW_BASKET).click()
    browser.find_element(*ProductPageLocators.QUANTITY_PRODUCTS).clear()
    browser.find_element(*ProductPageLocators.QUANTITY_PRODUCTS).send_keys('0')
    browser.find_element(*ProductPageLocators.BUTTON_UPDATE).click()
