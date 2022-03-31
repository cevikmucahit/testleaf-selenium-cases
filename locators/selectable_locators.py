from selenium.webdriver.common.by import By

SELECTABLE_URL = "http://www.leafground.com/pages/selectable.html"
LIST = (By.CSS_SELECTOR, "ol li")
SELECTED_LI = (By.CSS_SELECTOR, ".ui-widget-content.ui-selectee.ui-selected")