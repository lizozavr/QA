import time

from initial_page import BasePage
from site_locators import PageLocators, SearchResultLocators, CatalogLocators, ShoppingCartLocators
from selenium.webdriver.common.keys import Keys


class SearchHelper(BasePage):

    def enter_search_text(self, text):
        search_field = self.find_element(PageLocators.SEARCH_BOX)
        search_field.send_keys(text)
        return search_field

    def click_enter(self):
        self.find_element(PageLocators.SEARCH_BOX).send_keys(Keys.ENTER)

    def find_text(self):
        return self.find_element(SearchResultLocators.SEARCH_RESULT_HEADING).text


class CatalogOption(BasePage):
    def click_on_catalog(self):
        self.find_element(CatalogLocators.CATALOG).click()

    def click_on_apple_gadgets_option(self):
        time.sleep(10)
        self.find_element(CatalogLocators.APPLE_GADGETS).click()

    def find_text(self):
        return self.find_element(SearchResultLocators.SEARCH_RESULT_HEADING).text


class ShoppingCart(BasePage):

    def click_on_shopping_cart(self):
        time.sleep(10)
        self.find_element(ShoppingCartLocators.CART_LABEL).click()

    def find_text(self):
        return self.find_element(SearchResultLocators.CART_POPUP_TEXT).text
