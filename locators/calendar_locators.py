from selenium.webdriver.common.by import By

CALENDAR_URL = "http://www.leafground.com/pages/Calendar.html"
INPUT = (By.ID, "datepicker")
DAYS = (By.CSS_SELECTOR, ".ui-datepicker-calendar tbody td a")