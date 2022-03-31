import unittest

from selenium.webdriver import ActionChains

from config import browser
from locators.sortable_locators import SORTABLE_URL, LIST


class SortablePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(SORTABLE_URL)

    def test_sortable(self):
        sortable_list = self.driver.find_elements(*LIST)
        current_location = sortable_list[1].location

        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(sortable_list[0], 0, 50).perform()

        expected_location = sortable_list[0].location

        self.assertEqual(current_location, expected_location)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
