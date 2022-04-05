import time
import unittest

from config import browser
from locators.download_locators import DOWNLOAD_URL, EXEL_DOWNLOAD


class DownloadPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(DOWNLOAD_URL)

    def test_download_files(self):
        download_links = self.driver.find_elements(*EXEL_DOWNLOAD)
        exel_download = download_links[1]
        exel_download.click()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
