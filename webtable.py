import unittest

from config import browser
from selenium.webdriver.common.action_chains import ActionChains
from locators.advance_web_table_locators import ADVANCE_URL, NAME_LIST, NAME_HEAD


class TablePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(ADVANCE_URL)

    def test_sortable(self):
        name_list = self.driver.find_elements(*NAME_LIST)

        for name in name_list:
            print(name.text)

        name_head = self.driver.find_element(*NAME_HEAD)

        action = ActionChains(self.driver)

        action.move_to_element(name_head).click().perform()

        for name_2 in name_list:
            print(name_2.text)

        self.assertNotEqual(name.text, name_2.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
