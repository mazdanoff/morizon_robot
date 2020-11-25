from hamcrest import assert_that, less_than, greater_than

from page_objects.morizon_pl import MorizonMainPage, MorizonResultsPage, MorizonOfferPage
from utils.browser_factory import BrowserFactory


class MorizonLibrary(object):

    def __init__(self, driver_name):
        self._driver = BrowserFactory().get(name=driver_name)

    def __del__(self):
        # there is no proper context manager for handling driver
        # so we just destroy it semi-manually when the library is not needed anymore
        # I learned to forgive myself, and you should forgive me, too :)
        self._driver.close()
        self._driver.quit()

    def open_main_page(self, url):
        page = MorizonMainPage(self._driver, url=url)
        page.open().wait_for_page_to_load()
        assert_that(page.is_page_displayed(), "Main page is not displayed")
        page.wait_for_cookies_popup()
        page.accept_cookies_button.click()

    def set_location(self, location):
        page = MorizonMainPage(self._driver)
        if not page.min_price_field.is_displayed():
            page.open_price_fields()
        page.location_field.value = location

    def set_minimum_value(self, value):
        page = MorizonMainPage(self._driver)
        if not page.min_price_field.is_displayed():
            page.open_price_fields()
        page.min_price_field.value = value

    def set_maximum_value(self, value):
        page = MorizonMainPage(self._driver)
        page.max_price_field.value = value

    def click_search_button(self):
        page = MorizonMainPage(self._driver)
        page.search_button.click()

    def click_first_result(self):
        page = MorizonResultsPage(self._driver).wait_for_page_to_load()
        assert_that(page.is_page_displayed(), "Results page is not displayed")
        page.results_list[0].price.click()

    def price_is_within_set_brackets(self, min_val, max_val):
        page = MorizonOfferPage(self._driver).wait_for_page_to_load()
        assert_that(page.is_page_displayed(), "A page with the offer is not displayed")
        actual_price = page.get_price()
        assert_that(actual_price, less_than(max_val))
        assert_that(actual_price, greater_than(min_val))
