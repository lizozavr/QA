from selenium.webdriver.common.by import By


class PageLocators:
    SEARCH_BOX = (By.ID, "header-big-screen-search-box")


class SearchResultLocators:
    SEARCH_RESULT_HEADING = (By.CLASS_NAME, "spell-correct")
    CONDITIONS = (By.LINK_TEXT, "Условия")


class СonditionLocators:
    GOODS_RETURN = (By.LINK_TEXT, "Возврат товаров")