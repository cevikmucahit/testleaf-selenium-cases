import unittest

from selenium.webdriver import ActionChains

from config import browser
from locators.draggable_locators import DRAGGABLE_URL, SOURCE_ELEMENT


class DraggablePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(DRAGGABLE_URL)

    def test_draggable(self):
        source_element = self.driver.find_element(*SOURCE_ELEMENT)
        current_location = source_element.location

        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(source_element, 150, 200).perform()

        location = source_element.location

        self.assertNotEqual(current_location, location)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
