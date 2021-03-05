from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert


class BasePage:

    def __init__(self, browser, timeout=20):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def alert_accept(self):
        Alert(self.browser).accept()
