import unittest

from selenium.webdriver import ActionChains

from config import browser
from locators.droppable_locators import DROPPABLE_URL, DRAG, DROP


class DroppablePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(DROPPABLE_URL)

    def test_droppable(self):
        drag = self.driver.find_element(*DRAG)
        drop = self.driver.find_element(*DROP)

        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()

        self.assertIn("Dropped!", drop.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
