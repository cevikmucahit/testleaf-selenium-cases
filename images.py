import requests
import unittest

from config import browser
from locators.images_locators import IMAGE_URL, HOME_IMAGE, BROKEN_IMAGE, MOUSE_IMAGE
from selenium.webdriver import ActionChains


class ImagePage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(IMAGE_URL)

    def test_click_image(self):
        self.driver.find_element(*HOME_IMAGE).click()

        expected_url = "http://www.leafground.com/home.html"

        self.assertEqual(self.driver.current_url, expected_url)

    def test_broken_image(self):
        image = self.driver.find_element(*BROKEN_IMAGE)

        r = requests.head(image.get_attribute("src"))

        self.assertTrue(r.status_code != 200)

    def test_mouse_control(self):
        image = self.driver.find_element(*MOUSE_IMAGE)
        expected_url = "http://www.leafground.com/home.html"

        actions = ActionChains(self.driver)
        actions.move_to_element(image)
        actions.click(image)
        actions.perform()

        self.assertEqual(expected_url, self.driver.current_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
