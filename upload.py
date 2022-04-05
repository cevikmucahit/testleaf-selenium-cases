import os
import unittest

from config import browser
from locators.upload_locators import UPLOAD_URL, UPLOAD_INPUT


class UploadPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(UPLOAD_URL)

    def test_upload_png(self):
        upload_input = self.driver.find_element(*UPLOAD_INPUT)
        upload_input.send_keys(os.getcwd() + "/image.jpg")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
