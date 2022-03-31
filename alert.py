import unittest

from config import browser
from locators.alert_locators import ALERT_URL, CLICK_ALERT, ALERT_GET_TEXT, RESULT, ALERT_INPUT, RESULT_1, \
    LINE_BREAKS_ALERT


class AlertPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(ALERT_URL)

    def test_click_alert(self):
        alert = self.driver.find_element(*CLICK_ALERT)
        alert.click()

        self.assertTrue(self.driver.switch_to.alert)

    def test_get_alert_text(self):
        button = self.driver.find_element(*ALERT_GET_TEXT)
        button.click()

        alert = self.driver.switch_to.alert
        alert.accept()

        result = self.driver.find_element(*RESULT)

        self.assertEqual(result.text, "You pressed OK!")

    def test_alert_prompt(self):
        button = self.driver.find_element(*ALERT_INPUT)
        button.click()

        text = "Mico"
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

        result = self.driver.find_element(*RESULT_1)

        self.assertIn(text, result.text)

    def test_line_breaks_in_alert(self):
        button = self.driver.find_element(*LINE_BREAKS_ALERT)
        button.click()

        alert = self.driver.switch_to.alert

        self.assertIn("\n", alert.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
