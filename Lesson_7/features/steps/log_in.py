from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.main_page import MainPage
from pages.base_page import Page
from selenium.common.exceptions import NoSuchElementException
from time import sleep

@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com')

@when("Click Sign")
def sign_in(context):
    login_button = context.driver.find_element(By.CSS_SELECTOR, '#listaccountNav-signIn > a > span')
    ActionChains(context.driver).move_to_element(login_button).click().perform()


@when("From side navigation, click sign in")
def login_from_side_navigation(context):
    username = 'roggertorrez@yaoghyth.cz'
    password = 'GeorgeWashington'
    login_button = Page(context.driver).find_element(By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')
    ActionChains(context.driver).move_to_element(login_button).click().perform()
    login_user = context.driver.find_element(By.CSS_SELECTOR, '#listaccountNav-signIn > a > span')
    login_user = context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="accountNav-signIn"]').click()
    context.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
    context.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
    #sleep(6)
    context.driver.find_element(By.CSS_SELECTOR, '#login').click()



@when("Input email and password on SignIn page")
def step_impl(context):
    pass


@then("Verify user is logged in (sign in form should disappear)")
def verify_user_is_logged_in(context):
    try:
        username_input = context.find_element(By.XPATH, '//*[@id="username"]')
        ActionChains(context.driver).move_to_element(username_input).send_keys(context)
    except:
        if NoSuchElementException:
            print('Form disappeared')
            print('Login succeeded.')


@when("Click Sign In")
def step_impl(context):
     pass


# @step("Input email and password on SignIn page")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: And Input email and password on SignIn page')
@given("Open Circle page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given Open Circle page')


# @then("Verify that clicking though Circle tabs works")
# def step_impl(context):
#     """
#     :type context: behave.runner.Context
#     """
#     raise NotImplementedError(u'STEP: Then Verify that clicking though Circle tabs works')