from selenium.webdriver.common.by import By

WINDOW_URL = "http://www.leafground.com/pages/Window.html"
WINDOW_BUTTON = (By.ID, "home")
MULTIPLE_WINDOW = (By.CSS_SELECTOR, "[onclick='openWindows()']")
CLOSE_NEW_WINDOWS = (By.ID, "color")
WAIT_BUTTON = (By.CSS_SELECTOR, "[onclick='openWindowsWithWait();']")