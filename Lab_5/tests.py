import time
from page_objects import SearchHelper, ConditionsSearch
from selenium import webdriver
from unittest import TestCase


class Test_Next(TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Safari()
        self.browser.get("https://www.next.ua/ru")
        self.browser.maximize_window()
        time.sleep(5)

    def test_search_field_hat(self):
        search_request = "шапка"
        main_page = SearchHelper(self.browser)
        main_page.enter_search_text(search_request)
        main_page.click_enter()
        assert search_request in main_page.find_text()

    def test_search_field_dress(self):
        search_request = "платье"
        main_page = SearchHelper(self.browser)
        main_page.enter_search_text(search_request)
        main_page.click_enter()
        assert search_request in main_page.find_text()

    def test_search_tab_conditions(self):
        tab_name = "Условия"
        main_page = ConditionsSearch(self.browser)
        main_page.click_on_conditions_link()
        response_category_name = main_page.find_text()
        assert response_category_name.lower() == tab_name.lower()

    def close_browser(self):
        self.browser.close()