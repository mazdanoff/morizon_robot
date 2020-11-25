from selenium.webdriver.common.by import By


class MorizonMainPageLocators:

    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//div[@class='qc-cmp2-summary-buttons']//button[text()='ZGADZAM SIĘ']")

    LOCATION_FIELD = (By.CSS_SELECTOR, "input#ps_location_text")
    PRICE_FIELDS = (By.CSS_SELECTOR, "#ps_price p")
    MIN_PRICE_FIELD = (By.CSS_SELECTOR, "input#ps_price_from")
    MAX_PRICE_FIELD = (By.CSS_SELECTOR, "input#ps_price_to")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.submitKey")
