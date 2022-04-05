import unittest

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from config import browser
from locators.window_locators import WINDOW_URL, WINDOW_BUTTON, MULTIPLE_WINDOW, CLOSE_NEW_WINDOWS, WAIT_BUTTON


class WindowPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(WINDOW_URL)

    def test_click_window(self):
        button = self.driver.find_element(*WINDOW_BUTTON)
        button.click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        expected_url = "http://www.leafground.com/home.html"

        self.assertEqual(self.driver.current_url, expected_url)

    def test_multiple_window(self):
        button = self.driver.find_element(*MULTIPLE_WINDOW)
        button.click()

        handles = self.driver.window_handles

        self.assertEqual(3, len(handles))

    def test_close_new_windows(self):
        self.driver.find_element(*CLOSE_NEW_WINDOWS).click()

        for idx, window in enumerate(self.driver.window_handles):
            if idx != 0:
                self.driver.switch_to.window(window)
                self.driver.close()

        self.assertEqual(1, len(self.driver.window_handles))

    def test_wait_for_window(self):
        wait = WebDriverWait(self.driver, 5)
        button = self.driver.find_element(*WAIT_BUTTON)
        button.click()

        expected_window_count = 3

        wait.until(ec.number_of_windows_to_be(expected_window_count))

        self.assertEqual(expected_window_count, len(self.driver.window_handles))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
