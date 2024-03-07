from behave import *

@given('Open target.com')
def open_target(context):
    context.main_page.open_main()


@when("Click Sign In")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When Click Sign In')


@step("From side navigation, click sign in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And From side navigation, click sign in')


@step("Input email and password on SignIn page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Input email and password on SignIn page')


@then("Verify user is logged in (sign in form should disappear)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Verify user is logged in (sign in form should disappear)')