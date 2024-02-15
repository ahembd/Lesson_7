from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

NEW_USER_NAME = (By.ID, 'ap_customer_name')
NEW_EMAIL = (By.ID, 'ap_email')
NEW_PASSWORD = (By.ID, 'ap_password')
PASSWORD_CHECK = (By.ID, 'ap_password_check')
SEARCH_SUBMIT = (By.ID, 'continue')
OTP_CODE = (By.ID, 'cvf-input-code')

@given('Open Amazon page')
def open_google(context):
    context.driver.get('https://www.amazon.com/ap/register?openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid'
                       '.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Drhf_sign_in&openid.assoc_handle=usflex/')


@when('Input {new_user_name} into ap_customer field')
def input_search(context, new_user_name):
    search = context.driver.find_element(*NEW_USER_NAME)
    search.clear()
    search.send_keys(new_user_name)
    sleep(4)

@when('Input {new_password} into ap_password field')
def input_search(context, new_password):
    search = context.driver.find_element(*NEW_PASSWORD)
    search.clear()
    search.send_keys(new_password)
    sleep(4)

@when('Input {password_check} into ap_password_check field')
def input_search(context, password_check):
    search = context.driver.find_element(*PASSWORD_CHECK)
    search.clear()
    search.send_keys(password_check)
    sleep(4)

@when('Click on submit icon')
def click_submit_button(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)

@then('One time password has been sent to your email.')
def verify_found_results_text(context):
    #OTP Code ('one time password button will appear.
    OTP_CODE != None