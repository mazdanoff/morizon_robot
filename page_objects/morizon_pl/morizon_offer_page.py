import re

from utils.page_elements import TextElement
from ..abstract import BasePage
from .morizon_offer_page_locators import MorizonOfferPageLocators as Locators


class MorizonOfferPage(BasePage):

    price = TextElement(*Locators.PRICE)

    def is_page_displayed(self):
        return self.price.is_displayed()

    def wait_for_page_to_load(self):
        self.wait_for_visibility_of_element_located(*Locators.PRICE, timeout=10)
        return self

    def get_price(self):
        actual_price = self.price.text
        actual_price = re.search(r'(.*) zł', actual_price).group(1)
        if " " in actual_price:
            actual_price = actual_price.replace(" ", "")
        return int(actual_price)
