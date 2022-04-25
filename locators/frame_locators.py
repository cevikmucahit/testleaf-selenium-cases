from selenium.webdriver.common.by import By

FRAME_URL = "http://www.leafground.com/pages/frame.html"
CLICK_FRAME = (By.ID, "Click")
FRAME = (By.CSS_SELECTOR, "[src='default.html']")
FRAME_IN_1 = (By.CSS_SELECTOR, "[src='page.html']")
FRAME_IN_2 = (By.CSS_SELECTOR, "[src='nested.html']")
CLICK_FRAME_2 = (By.ID, "Click1")
MAIN_FRAME = (By.CSS_SELECTOR, '[src="countframes.html"]')
FRAMES = (By.TAG_NAME, "iframe")
