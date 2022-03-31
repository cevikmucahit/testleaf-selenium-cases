from selenium.webdriver.common.by import By

ALERT_URL = "http://www.leafground.com/pages/Alert.html"
CLICK_ALERT = (By.CSS_SELECTOR, "[onclick='normalAlert()']")
ALERT_GET_TEXT = (By.CSS_SELECTOR, "[onclick='confirmAlert()']")
RESULT = (By.ID, "result")
RESULT_1 = (By.ID, "result1")
ALERT_INPUT = (By.CSS_SELECTOR, "[onclick='confirmPrompt()']")
LINE_BREAKS_ALERT = (By.CSS_SELECTOR, "[onclick='lineBreaks()']")
BUTTON_ALERT = (By.CSS_SELECTOR, "[onclick='sweetalert()']")

