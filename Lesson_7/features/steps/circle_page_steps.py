from selenium.webdriver.common.by import By
from pages.base_page import Page
from behave import given, then
from pages.cart_page import CartPage
from pages.base_page import Page
from pages.circle_page import CirclePage


@given('Open Circle2 page')
def open_circle2_page(self):
    print('here')
    CirclePage.open_circle(self)

@then("Verify that clicking through Circle2 tabs works")
def verify_clicking_though_circle_page(context):
    print('in then, *CirclePage.BONUS_TAB == ' + str(CirclePage.BONUS_TAB))

    @then('Verify that clicking though Circle tabs works')
    def verify_can_click_thru_tabs(context):
        print('in then, verify_can_click_thru_tabs')
        context.app.circle_page.verify_can_click_thru_tabs()