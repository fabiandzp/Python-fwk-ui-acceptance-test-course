from behave import *
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

use_step_matcher('re') #maps the steps to diferents variables

base_url = 'https://qa-btn-app.herokuapp.com'
#base_url = 'http://127.0.0.1:5000'

@given('I am on the homepage')
def step_impl(context):
    # Se crea la propiedad browser en la variable contexto
    # context.driver = webdriver.Chrome() # It will look in the web driver in the path
    context.driver = webdriver.Chrome(chrome_options=chrome_options)  # It will look in the web driver in the path
    context.driver.get(base_url)


@given('I am on the blog page')
def step_impl(context):
    # Se crea la propiedad browser en la variable contexto
    # context.driver = webdriver.Chrome() # It will look in the web driver in the path
    context.driver = webdriver.Chrome(chrome_options=chrome_options)
    context.driver.get(base_url+'/blog')


@then('I am on the blog page')
def step_impl(context): #Context property, se pueden almacenar valores en esa propiedad si se requiere
    expected_url = base_url+'/blog'
    assert context.driver.current_url == expected_url #Usamos python assert by default


@then('I am on the homepage')
def step_impl(context): #Context property, se pueden almacenar valores en esa propiedad si se requiere
    expected_url = base_url+'/'
    assert context.driver.current_url == expected_url #Usamos python assert by default