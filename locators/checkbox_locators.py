from selenium.webdriver.common.by import By

CHEKCBOX_URL = "http://www.leafground.com/pages/checkbox.html"
VB_CHECKBOX = (By.CSS_SELECTOR, ".innerblock .example:nth-of-type(1) input:nth-of-type(2)")
C_CHECKBOX = (By.CSS_SELECTOR, ".innerblock .example:nth-of-type(1) input:nth-of-type(4)")
CHECKED_CHECKBOX = (By.CSS_SELECTOR, ".innerblock .example:nth-of-type(2) input")
DESELECT_CHECKBOX = (By.CSS_SELECTOR, ".innerblock .example:nth-of-type(3) input:nth-of-type(1)")
ALl_CHECKBOX = (By.CSS_SELECTOR, ".example:nth-of-type(4) input")
