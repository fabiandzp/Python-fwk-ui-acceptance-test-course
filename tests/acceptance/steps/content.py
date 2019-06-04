from behave import *
from selenium.webdriver.common.by import By


#from code.tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')

@then('There is a title shown on the page')
def step_impl(context):
    title_tag = context.driver.find_element(By.TAG_NAME, 'h1')
    assert title_tag.is_displayed()
    #page = BasePage(context.driver)
    #assert page.title.is_displayed() # This just check that the user can see the tags inside of the window

@step('The title tag has content "(.*)"') #@Step decorator could be used anywhere and can start with and
def step_impl(context, content):
    title_tag = context.driver.find_element(By.TAG_NAME, 'h1')
    assert title_tag.text == content

    #page = BasePage(context.driver)
    #assert page.title.text == content