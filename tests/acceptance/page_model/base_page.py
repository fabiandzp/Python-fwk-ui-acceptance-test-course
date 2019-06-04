from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    #@property
    #def url(self):
    #    return 'http://127.0.0.1:5000'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE) # El asterisco des construye la tupla y pasa dos valores

    #@property
    #def navigation(self):
    #    return self.driver.find_element(*BasePageLocators.NAV_LINKS)