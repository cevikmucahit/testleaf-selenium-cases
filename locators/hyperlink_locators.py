from selenium.webdriver.common.by import By

HYPERLINK_URL = "http://www.leafground.com/pages/Link.html"
HOME_LINK = (By.CSS_SELECTOR, "[link='blue']")
FIND_LINK = (By.CSS_SELECTOR, "[href='Button.html']")
ERROR_LINK = (By.CSS_SELECTOR, "[href='error.html']")
COUNT_LINK = (By.TAG_NAME, "a")



