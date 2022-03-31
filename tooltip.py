import unittest
import time

from selenium.webdriver import Keys

from config import browser

from locators.tooltip_locators import TOOLTIP_URL, INPUT


class TooltipPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(TOOLTIP_URL)

    def test_interact_with_tooltip(self):
        tooltip_input = self.driver.find_element(*INPUT)
        tooltip_input.send_keys("mucahit")
        time.sleep(2)
        tooltip_input.send_keys(Keys.ARROW_DOWN)

        tooltip_input.send_keys(Keys.ENTER)

        self.assertIn("mucahit", tooltip_input.get_attribute("value"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
