from .locators import ProductAddAndEditPageLocators
from .base_page import BasePage


class ProductsAddAndEditPage(BasePage):
    def general_info(self, product_name, description, meta_tag, meta_tag_description, meta_tag_keywords, product_tags):
        self.browser.find_element(*ProductAddAndEditPageLocators.PRODUCT_NAME_FIELD).send_keys(product_name)
        self.browser.find_element(*ProductAddAndEditPageLocators.DESCRIPTION_FIELD).clear()
        self.browser.find_element(*ProductAddAndEditPageLocators.DESCRIPTION_FIELD).send_keys(description)
        self.browser.find_element(*ProductAddAndEditPageLocators.META_TAG_FIELD).send_keys(meta_tag)
        self.browser.find_element(*ProductAddAndEditPageLocators.META_TAG_DESCRIPTION_FIELD).send_keys(meta_tag_description)
        self.browser.find_element(*ProductAddAndEditPageLocators.META_TAG_KEYWORDS_FIELD).send_keys(meta_tag_keywords)
        self.browser.find_element(*ProductAddAndEditPageLocators.PRODUCT_TAGS_FIELD).send_keys(product_tags)
        return self

    def data_info(self, model):
        self.browser.find_element(*ProductAddAndEditPageLocators.DATA_PAGE).click()
        self.browser.find_element(*ProductAddAndEditPageLocators.MODEL_FIELD).send_keys(model)
        return self

    def attribute_info_remove(self):
        self.browser.find_element(*ProductAddAndEditPageLocators.ATTRIBUTE_PAGE).click()
        self.browser.find_element(*ProductAddAndEditPageLocators.REMOVE_2_BUTTON).click()
        return self

    def option_add_delivery_date(self):
        self.browser.find_element(*ProductAddAndEditPageLocators.OPTION_PAGE).click()
        self.browser.find_element(*ProductAddAndEditPageLocators.INPUT_OPTION).send_keys("Delivery")
        self.browser.find_element(*ProductAddAndEditPageLocators.DELIVERY_DATE).click()
        return self

    def option_required_no_select(self):
        self.browser.find_element(*ProductAddAndEditPageLocators.OPTION_PAGE).click()
        self.browser.find_element(*ProductAddAndEditPageLocators.REQUIRED_SELECT).click()
        self.browser.find_element(*ProductAddAndEditPageLocators.NO_SELECT).click()
        return self

    def get_monitor_category_link(self):
        self.browser.find_element(*ProductAddAndEditPageLocators.LINKS_PAGE).click()
        self.browser.find_element(*ProductAddAndEditPageLocators.CATEGORIES_FIELD).click()
        self.browser.find_element(*ProductAddAndEditPageLocators.MONITOR_CATEGORIES_SELECT).click()
        return self

    def save(self):
        self.browser.find_element(*ProductAddAndEditPageLocators.SAVE_BUTTON).click()
        return self

    def should_be_success_alert(self):
        assert self.is_element_present(*ProductAddAndEditPageLocators.SUCCESS_ALERT), "Assert is not presented"
        return self
