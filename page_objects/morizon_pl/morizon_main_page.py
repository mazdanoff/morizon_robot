from utils.page_elements import Button, InputField
from ..abstract import BasePage

from .morizon_main_page_locators import MorizonMainPageLocators as Locators


class MorizonMainPage(BasePage):

    accept_cookies_button = Button(*Locators.ACCEPT_COOKIES_BUTTON)

    location_field = InputField(*Locators.LOCATION_FIELD)

    min_price_field = InputField(*Locators.MIN_PRICE_FIELD)
    max_price_field = InputField(*Locators.MAX_PRICE_FIELD)
    search_button = Button(*Locators.SEARCH_BUTTON)

    def is_page_displayed(self):
        return self.location_field.is_displayed()

    def wait_for_page_to_load(self):
        self.wait_for_visibility_of_element_located(*Locators.LOCATION_FIELD, timeout=10)

    def wait_for_cookies_popup(self):
        self.wait_for_visibility_of_element_located(*Locators.ACCEPT_COOKIES_BUTTON, timeout=10)

    def open_price_fields(self):
        price_fields = self.find_element(*Locators.PRICE_FIELDS)
        price_fields.click()
        self.wait_for_visibility_of_element_located(*Locators.MIN_PRICE_FIELD, timeout=5)
