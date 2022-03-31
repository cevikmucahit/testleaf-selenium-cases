from selenium.webdriver.common.by import By

TABLE_URL = "http://www.leafground.com/pages/table.html"
TABLE_COLUMN = (By.CSS_SELECTOR, "th")
TABLE_ROW = (By.CSS_SELECTOR, "tr")
PROGRESS_COLUMN = (By.CSS_SELECTOR, "tr:nth-of-type(3) td:nth-of-type(2)")
COMPLETED_PROGRESS = (By.CSS_SELECTOR, "tr :nth-of-type(2):not(th)")


