import unittest

from config import browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.wait_for_alert_locators import WAITALERT_URL, ALERT_BUTTON

class WaitalertPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(WAITALERT_URL)

    def test_wait_for_alert(self):
        alert_button = self.driver.find_element(*ALERT_BUTTON)
        alert_button.click()

        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert


        self.assertIn("Hurray",alert.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()