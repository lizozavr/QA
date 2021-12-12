import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import TestCase


class Test_Next(TestCase):
    def test_search_hat(self):
        search_request = "шапка"
        url = 'https://www.next.ua/ru'
        browser = webdriver.Safari()

        browser.get(url)
        time.sleep(5)
        browser.find_element(by=By.ID, value='header-big-screen-search-box').send_keys(search_request)
        browser.find_element(by=By.ID, value='header-big-screen-search-box').send_keys(Keys.ENTER)
        time.sleep(5)

        actualResult = browser.find_element(by=By.CLASS_NAME, value='spell-correct').text

        assert search_request in actualResult

        browser.close()

    def test_search_return_conditions(self):
        search_text = "Условия"
        url = 'https://www.next.ua/ru'
        browser = webdriver.Safari()

        browser.get(url)
        time.sleep(5)
        browser.find_element(by=By.LINK_TEXT, value="Возврат товаров").click()
        time.sleep(5)
        actualResult = browser.find_element(by=By.LINK_TEXT, value=search_text).text
        time.sleep(5)

        assert search_text in actualResult

        browser.close()
