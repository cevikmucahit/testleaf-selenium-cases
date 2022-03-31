import unittest

from config import browser
from locators.radio_locators import RADIOBUTTON_URL, CLICK_RADIO_BUTTON, CHECKED_RADIO_BUTTON, GROUP_RADIO_BUTTON


class RadioButtonPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(RADIOBUTTON_URL)

    def test_click_radio_button(self):
        button = self.driver.find_element(*CLICK_RADIO_BUTTON)
        button.click()

        self.assertTrue(button.get_attribute("checked"))

    def test_radio_button_is_checked(self):
        button = self.driver.find_element(*CHECKED_RADIO_BUTTON)

        self.assertTrue(button.get_attribute("checked"))

    def test_radio_group_select(self):
        radio_buttons = self.driver.find_elements(*GROUP_RADIO_BUTTON)
        is_checked = False

        for radio in radio_buttons:
            if radio.get_attribute("checked"):
                is_checked = True

        self.assertTrue(is_checked)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
