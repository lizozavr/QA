from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://www.next.ua/ru"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(expected_conditions.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(expected_conditions.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def go_to_webpage(self):
        return self.browser.get(self.base_url)
