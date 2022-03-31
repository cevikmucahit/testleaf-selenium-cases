from selenium.webdriver.common.by import By

DROPDOWN_URL = "http://www.leafground.com/pages/Dropdown.html"
INDEX_DROPDOWN = (By.ID, "dropdown1")
TEXT_DROPDOWN = (By.NAME, "dropdown2")
VALUE_DROPDOWN = (By.NAME, "dropdown3")
OPTIONS_COUNT_DROPDOWN = (By.CLASS_NAME, "dropdown")
KEYS_DROPDOWN = (By.CSS_SELECTOR, ".example:nth-of-type(5) select")
MULTIPLE_DROPDOWN = (By.CSS_SELECTOR, "[multiple]")
