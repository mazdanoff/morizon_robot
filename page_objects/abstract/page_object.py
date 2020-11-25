import time
from abc import ABCMeta

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageObject(metaclass=ABCMeta):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def is_element_located_present(self, by, value, context=None):
        context = context or self.driver
        try:
            context.find_element(by=by, value=value)
        except NoSuchElementException:
            return False
        return True

    def find_element(self, by, value, context=None):
        context = context or self.driver
        return context.find_element(by, value)

    def find_elements(self, by, value, context=None):
        context = context or self.driver
        return context.find_elements(by, value)

    @staticmethod
    def wait(timeout):
        time.sleep(timeout)

    def wait_for_presence_of_element_located(self, how, what, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def wait_for_visibility_of_element_located(self, how, what, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True
