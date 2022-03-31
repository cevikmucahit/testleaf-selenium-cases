import unittest

from selenium.webdriver.common.keys import Keys
from config import browser
from locators.edits_locators import EDITS_URL, EMAIL_INPUT, TAB_INPUT, GET_VALUE_INPUT, CLEAR_INPUT, DISABLED_INPUT


class EditsPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(EDITS_URL)

    def test_enter_email(self):
        email = "mmmico@hotmail.com"
        email_input = self.driver.find_element(*EMAIL_INPUT)

        email_input.send_keys(email)

        self.assertEqual(email_input.get_attribute("value"), email)

    def test_press_tab(self):
        tab_input = self.driver.find_element(*TAB_INPUT)
        tab_input.click()
        tab_input.send_keys(Keys.TAB)

        focused_input = self.driver.find_element(*GET_VALUE_INPUT)

        self.assertTrue(focused_input == self.driver.switch_to.active_element)

    def test_get_input_value(self):
        value_input = self.driver.find_element(*GET_VALUE_INPUT)
        expected_value = "TestLeaf"

        self.assertEqual(value_input.get_attribute("value"), expected_value)

    def test_clear_input(self):
        clear_input = self.driver.find_element(*CLEAR_INPUT)
        clear_input.clear()

        self.assertEqual(clear_input.get_attribute("value"), "")

    def test_input_is_disabled(self):
        disabled_input = self.driver.find_element(*DISABLED_INPUT)

        self.assertTrue(disabled_input.get_attribute("disabled") == "true")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
