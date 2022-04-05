import time
import unittest

from selenium.webdriver import Keys

from config import browser
from locators.autocomplete_locators import AUTOCOMPLETE_URL, INPUT


class AutoCompletePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(AUTOCOMPLETE_URL)

    def test_autocomplete(self):
        autocomplete_input = self.driver.find_element(*INPUT)
        autocomplete_input.click()
        autocomplete_input.send_keys("se")

        time.sleep(3)

        autocomplete_input.send_keys(Keys.ARROW_DOWN)
        autocomplete_input.send_keys(Keys.ENTER)

        self.assertIn("Selenium", autocomplete_input.get_attribute("value"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
