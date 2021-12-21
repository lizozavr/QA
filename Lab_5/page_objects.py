from initial_page import BasePage
from site_locators import PageLocators, SearchResultLocators, СonditionLocators
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


class ConditionsSearch(BasePage):

    def click_on_conditions_link(self):
        self.find_element(СonditionLocators.GOODS_RETURN).click()

    def find_text(self):
        return self.find_element(SearchResultLocators.CONDITIONS).text
