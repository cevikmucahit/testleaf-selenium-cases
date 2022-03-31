import unittest

from config import browser
from selenium.webdriver import Keys

from locators.dropdown_locators import DROPDOWN_URL, INDEX_DROPDOWN, TEXT_DROPDOWN, VALUE_DROPDOWN, \
    OPTIONS_COUNT_DROPDOWN, KEYS_DROPDOWN, MULTIPLE_DROPDOWN
from selenium.webdriver.support.ui import Select


class DropdownPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(DROPDOWN_URL)

    def test_dropdown_select_by_index(self):
        dropdown = Select(self.driver.find_element(*INDEX_DROPDOWN))
        dropdown.select_by_index(0)

        self.assertEqual(0, int(dropdown.first_selected_option.get_attribute("value")))

    def test_dropdown_select_by_text(self):
        dropdown = Select(self.driver.find_element(*TEXT_DROPDOWN))
        dropdown.select_by_visible_text("Selenium")

        self.assertEqual("Selenium", dropdown.first_selected_option.text)

    def test_dropdown_select_by_value(self):
        dropdown = Select(self.driver.find_element(*VALUE_DROPDOWN))
        dropdown.select_by_value("2")

        self.assertEqual(2, int(dropdown.first_selected_option.get_attribute("value")))

    def test_get_dropdown_options_count(self):
        dropdown = Select(self.driver.find_element(*OPTIONS_COUNT_DROPDOWN))

        self.assertEqual(5, len(dropdown.options))

    def test_dropdown_select_by_keys(self):
        dropdown = self.driver.find_element(*KEYS_DROPDOWN)

        dropdown.click()
        dropdown.send_keys(Keys.ARROW_DOWN)
        dropdown.send_keys(Keys.ARROW_DOWN)
        dropdown.send_keys(Keys.ENTER)

        get_selected_text = Select(dropdown).first_selected_option.text

        self.assertEqual("Appium", get_selected_text)

    def test_dropdown_is_multiple(self):
        dropdown = Select(self.driver.find_element(*MULTIPLE_DROPDOWN))

        self.assertTrue(dropdown.is_multiple)

    def test_dropdown_multiple_select(self):
        dropdown = Select(self.driver.find_element(*MULTIPLE_DROPDOWN))

        dropdown.select_by_index(0)
        dropdown.select_by_index(2)

        self.assertEqual(2, len(dropdown.all_selected_options))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
