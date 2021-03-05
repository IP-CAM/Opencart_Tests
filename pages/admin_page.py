from .base_page import BasePage
from .locators import AdminPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AdminPage(BasePage):
    def go_to_product_page(self):
        self.browser.find_element(*AdminPageLocators.CATALOG_BUTTON).click()
        self.browser.find_element(*AdminPageLocators.PRODUCT_BUTTON).click()
        return self

    def add_product(self):
        self.browser.find_element(*AdminPageLocators.ADD_NEW_BUTTON).click()
        return self

    def edit_product(self, product_number):
        self.browser.find_elements(*AdminPageLocators.EDIT_BUTTONS).pop(product_number).click()
        return self

    def delete_product(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-danger"]')))
        self.browser.find_element(*AdminPageLocators.DELETE_BUTTON).click()
        return self

    def new_product_choice(self, checkbox_number):
        self.browser.find_elements(*AdminPageLocators.NEW_PRODUCT_CHECKBOX).pop(checkbox_number).click()

