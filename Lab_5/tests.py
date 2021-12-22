import time
from page_objects import SearchHelper, CatalogOption, ShoppingCart
from selenium import webdriver
from unittest import TestCase


class Test_Next(TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Safari()
        self.browser.get("https://touch.com.ua")
        self.browser.maximize_window()
        time.sleep(5)

    def close_browser(self):
        self.browser.close()

    def test_search_field(self):
        search_request = "телефон"
        main_page = SearchHelper(self.browser)
        main_page.enter_search_text(search_request)
        main_page.click_enter()
        assert search_request in main_page.find_text()
        self.close_browser()

    def test_catalog_option(self):
        option_name = "Техника Apple"
        main_page = CatalogOption(self.browser)
        main_page.click_on_catalog()
        main_page.click_on_apple_gadgets_option()
        response_catalog_name = main_page.find_text()
        assert response_catalog_name.lower() == option_name.lower()
        self.close_browser()

    def test_is_shopping_cart_empty(self):
        empty_cart_text = "Ваша корзина пуста"
        main_page = ShoppingCart(self.browser)
        main_page.click_on_shopping_cart()
        response_cart_popup_text = main_page.find_text()
        assert empty_cart_text in response_cart_popup_text
        self.close_browser()