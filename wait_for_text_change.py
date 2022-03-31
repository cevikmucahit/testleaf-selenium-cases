import unittest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import browser
from locators.textchance_locators import TEXTCHANGE_URL, BUTTON


class TextchangePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(TEXTCHANGE_URL)

    def test_text_change(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.text_to_be_present_in_element(BUTTON, "Click ME!"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
