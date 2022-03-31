import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import browser
from locators.disappear_locators import DISAPPEAR_URL, DISAPPEARANCE_ELEMENT


class DisappearPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(DISAPPEAR_URL)

    def test_wait_for_element_disappearance(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(DISAPPEARANCE_ELEMENT))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
