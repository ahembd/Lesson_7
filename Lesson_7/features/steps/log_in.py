from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.main_page import MainPage
from selenium.common.exceptions import NoSuchElementException

@given('Open target.com')
def open_target(context):
    context.driver.get('https://www.target.com')

@when("Click Sign In")
def sign_in(context):
    login_button = context.driver.find_element(By.XPATH, '//*[@id="headerPrimary"]/a[4]/span')
    ActionChains(context.driver).move_to_element(login_button).click().perform()



@when("From side navigation, click sign in")
def login_from_side_navigation(context):
    username = 'roggertorrez@yaoghyth.cz'
    password = 'GeorgeWashington'
    login_button = context.driver.find_element(By.XPATH, '//*[@id="headerPrimary"]/a[4]/span')
    ActionChains(context.driver).move_to_element(login_button).click().perform()
    username_input = context.driver.find_element(By.XPATH, '//*[@id="username"]')
    password_input = context.driver.find_element(By.XPATH, '//*[@id="password"]')


    ActionChains(context.driver).move_to_element(username_input).send_keys(username)
    ActionChains(context.driver).move_to_element(password_input).send_keys(password)



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