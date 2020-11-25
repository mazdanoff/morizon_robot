"""Based on https://github.com/jenterkin/selenium-page-elements"""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class Element:
    def __init__(self, by: str, value: str, wait=None,
                 wait_timeout: int = 10, name: str = "Element"):
        self._by = by
        self._value = value
        self._obj = None
        self.wait = wait
        self.wait_timeout = wait_timeout
        self.name = name

    def __get__(self, obj, owner):
        self._obj = obj
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name}", by="{self._by}", value="{self._value}")'

    @property
    def _element(self):
        if self.wait is not None:
            # should be a selenium expected condition
            return WebDriverWait(self._obj.driver, self.wait_timeout).until(
                self.wait((self._by, self._value)))
        return self._obj.driver.find_element(self._by, self._value)

    def is_present(self) -> bool:
        try:
            return self._element
        except NoSuchElementException:
            return False

    def is_displayed(self) -> bool:
        try:
            return self._element.is_displayed()
        except NoSuchElementException:
            assert False, f"{self!r} is not present on page"

    def scroll_into_view(self):
        ActionChains(self._obj.driver).move_to_element(self._element).perform()
