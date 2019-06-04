from selenium.webdriver.common.by import By


class BlogPageLocators:
    ADD_POST_LINK = By.ID, 'add-post-link'
    POST_SECTION = By.ID, 'post'
    POST = By.CLASS_NAME, 'post-link'
