import unittest

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config import browser
from locators.appear_locators import APPEAR_URL, APPEAR_BUTTON


class AppearPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(APPEAR_URL)

    def test_appear_element(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(ec.text_to_be_present_in_element(APPEAR_BUTTON, "Voila! I'm here Guys"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
