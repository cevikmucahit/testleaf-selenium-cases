from selenium.webdriver.common.by import By

EDITS_URL = "http://www.leafground.com/pages/Edit.html"
EMAIL_INPUT = (By.ID, "email")
TAB_INPUT = (By.CSS_SELECTOR, "[value*='Append']")
GET_VALUE_INPUT = (By.CSS_SELECTOR, "[value*='T'][name='username']")
CLEAR_INPUT = (By.CSS_SELECTOR, "[value*='C'][name='username']")
DISABLED_INPUT = (By.CSS_SELECTOR, "[disabled]")
