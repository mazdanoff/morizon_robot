from abc import abstractmethod
from typing import Optional

from page_objects.abstract.page_object import PageObject


class NoURLProvidedException(Exception):
    pass


class BasePage(PageObject):

    def __init__(self, driver, url: Optional[str] = None):
        super().__init__(driver)
        self.url = url

    def open(self, url: Optional[str] = None):
        url = url or self.url
        if not url:
            raise NoURLProvidedException("No URL was provided while initializing page nor invoking 'open' method")
        self.driver.get(url)
        return self

    @abstractmethod
    def is_page_displayed(self):
        raise NotImplementedError

    @abstractmethod
    def wait_for_page_to_load(self):
        raise NotImplementedError
