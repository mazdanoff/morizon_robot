from selenium.webdriver.common.by import By
from selenium_datatable import DataTable, Column


class MorizonResultsList(DataTable):
    rows_locator = (By.CSS_SELECTOR,
                    ".listingBox.mainBox.propertyListingBox.content-box-main.col-xs-9 > section > .row.row--property-list")

    price = Column(By.CSS_SELECTOR,
                   ".row.row--property-list:nth-of-type({row}) p.single-result__price:nth-of-type(1)")
