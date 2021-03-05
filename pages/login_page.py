from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def login(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FIELD).send_keys('user')
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys('bitnami')
        self.browser.find_element(*LoginPageLocators.ENTER_BUTTON).click()
