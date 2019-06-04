from behave import *

use_step_matcher('re')

@when('I click on the link with id "(.*)"')
def step_impl(context, link_id):
    link = context.driver.find_element_by_id(link_id)
    link.click()

    #page = BasePage(context.driver)
    #links = page.navigation

    #matching_links = [l for l in links if l.text == link_text]

    #if len(matching_links) > 0:
    #    matching_links[0].click()
    #else:
    #    raise RuntimeError()