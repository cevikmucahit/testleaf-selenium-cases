import unittest

from config import browser
from locators.hyperlink_locators import HYPERLINK_URL, HOME_LINK, FIND_LINK, ERROR_LINK, COUNT_LINK


class HyperlinksPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(HYPERLINK_URL)

    def test_click_link(self):
        self.driver.find_element(*HOME_LINK).click()

        expected_url = "http://www.leafground.com/home.html"

        self.assertEqual(expected_url, self.driver.current_url)

    def test_get_href(self):
        link_attribute = self.driver.find_element(*FIND_LINK).get_attribute("href")

        self.assertEqual(link_attribute, "http://www.leafground.com/pages/Button.html")

    def test_error_link(self):
        error_anchor_href = self.driver.find_element(*ERROR_LINK).get_attribute("href")

        self.assertIn("error", error_anchor_href)

    def test_get_link_count(self):
        count_link = self.driver.find_elements(*COUNT_LINK)

        self.assertTrue(len(count_link) == 6)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
