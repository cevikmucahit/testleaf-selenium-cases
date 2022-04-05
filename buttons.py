import unittest

from config import browser
from locators.button_locators import BUTTONS_URL, HOME_BUTTON, COLOR_BUTTON, POSITION_BUTTON, SIZE_BUTTON


class ButtonsPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(BUTTONS_URL)

    def test_click_home(self):
        self.driver.find_element(*HOME_BUTTON).click()

        expected_url = "http://www.leafground.com/home.html"

        self.assertEqual(expected_url, self.driver.current_url)

    def test_get_button_color(self):
        button = self.driver.find_element(*COLOR_BUTTON)
        expected_color = "rgba(144, 238, 144, 1)"

        self.assertEqual(expected_color, button.value_of_css_property('background-color'))

    def test_get_button_position(self):
        button = self.driver.find_element(*POSITION_BUTTON)
        position = button.location

        self.assertIsNotNone(position)

    def test_get_button_size(self):
        button = self.driver.find_element(*SIZE_BUTTON)
        size = button.size

        self.assertIsNotNone(size)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
