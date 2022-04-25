import unittest

from selenium.webdriver.common.action_chains import ActionChains

from config import browser
from locators.tooltip_locators import TOOLTIP_URL, INPUT


class TooltipPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(TOOLTIP_URL)

    def test_interact_with_tooltip(self):
        tooltip_input = self.driver.find_element(*INPUT)
        tooltip_input_attribute = tooltip_input.get_attribute("title")

        action = ActionChains(self.driver)
        action.move_to_element(tooltip_input).perform()

        self.assertEqual(tooltip_input_attribute, "Enter your Name")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
