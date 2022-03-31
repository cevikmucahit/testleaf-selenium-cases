from selenium.webdriver.common.by import By

RADIOBUTTON_URL = "http://www.leafground.com/pages/radio.html"
CLICK_RADIO_BUTTON = (By.ID, "yes")
CHECKED_RADIO_BUTTON = (By.CSS_SELECTOR, "[name='news']:nth-of-type(2)")
GROUP_RADIO_BUTTON = (By.CSS_SELECTOR, ".example:nth-of-type(3) input")
