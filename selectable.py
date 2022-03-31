import unittest

from selenium.webdriver import ActionChains

from config import browser
from locators.selectable_locators import SELECTABLE_URL, LIST, SELECTED_LI


class SelectablePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(SELECTABLE_URL)

    def test_all_select_list(self):
        item_list = self.driver.find_element(*LIST)

        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(item_list, 0, 230).perform()

        selected_li = self.driver.find_elements(*SELECTED_LI)

        self.assertEqual(7, len(selected_li))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
