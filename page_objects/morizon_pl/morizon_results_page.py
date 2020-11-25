from ..abstract import BasePage

from .morizon_results_list import MorizonResultsList
from .morizon_results_page_locators import MorizonResultsPageLocators as Locators


class MorizonResultsPage(BasePage):

    results_list = MorizonResultsList(*Locators.RESULTS_LIST)

    def is_page_displayed(self):
        return self.is_element_located_present(*Locators.RESULTS_LIST)

    def wait_for_page_to_load(self):
        self.wait_for_visibility_of_element_located(*Locators.RESULTS_LIST, timeout=10)
        return self
