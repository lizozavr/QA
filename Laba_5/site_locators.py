from selenium.webdriver.common.by import By


class PageLocators:
    SEARCH_BOX = (By.ID, "searchQuery")


class SearchResultLocators:
    SEARCH_RESULT_HEADING = (By.CLASS_NAME, "changeName")
    CART_POPUP_TEXT = (By.CLASS_NAME, "modal-cart")


class ShoppingCartLocators:
    CART_LABEL = (By.CLASS_NAME, "cartLabel")


class CatalogLocators:
    CATALOG = (By.ID, "catalogMenuHeading")
    APPLE_GADGETS = (By.LINK_TEXT, "Техника Apple")
