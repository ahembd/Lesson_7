from pages.base_page import Page
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


class Application:
    def __init__(context, driver):
        context.page = Page(driver)
        context.cart_page = CartPage(driver)
        context.circle_page = CirclePage(driver)
        context.header = Header(driver)
        context.main_page = MainPage(driver)
        context.search_results_page = SearchResultsPage(driver)