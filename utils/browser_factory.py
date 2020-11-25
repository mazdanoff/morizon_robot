import os
from contextlib import contextmanager

from selenium import webdriver
from msedge.selenium_tools import EdgeOptions

from conf import path_conf as path

LOG_DIR = path.LOG_DIR


if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)


class BrowserFactoryError(Exception):
    pass


class BrowserFactory:

    def __init__(self):
        self._browser = dict()
        self._register_driver("chrome", chrome_builder)
        self._register_driver("edge", edge_builder)
        self._register_driver("firefox", firefox_builder)

    def _register_driver(self, name, browser):
        self._browser[name] = browser

    def get(self, name, headless=False, **kwargs):
        """Returns WebDriver instance"""
        # TODO: proper contextmanager based on pytest fixtures
        name = name.lower()
        driver_builder = self._browser.get(name)
        if not driver_builder:
            raise BrowserFactoryError(f"'{name}' is not recognized as a supported driver")

        driver = driver_builder(headless=headless, **kwargs)
        if driver:
            driver.maximize_window()
        return driver


def chrome_builder(headless=False, **kwargs):

    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.headless = True
    service_args = ["--verbose",
                    f"--log-path={LOG_DIR}/chrome_driver.log"]
    driver = webdriver.Chrome(options=chrome_options,
                              service_args=service_args)
    return driver


def edge_builder(headless=False, **kwargs):
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    if headless:
        edge_options.headless = True
    service_log_path = f"{LOG_DIR}/edge_driver.log"
    driver = webdriver.Edge(edge_options,
                            service_log_path=service_log_path)
    return driver


def firefox_builder(headless=False, **kwargs):
    firefox_options = webdriver.FirefoxOptions()
    if headless:
        firefox_options.headless = True
    service_log_path = f"{LOG_DIR}/firefox_driver.log"
    driver = webdriver.Firefox(firefox_options, service_log_path=service_log_path)
    return driver
