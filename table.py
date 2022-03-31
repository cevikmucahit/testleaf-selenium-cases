import unittest
from locators.table_locators import TABLE_URL, TABLE_COLUMN, TABLE_ROW, PROGRESS_COLUMN, COMPLETED_PROGRESS
from config import browser


class TablePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(TABLE_URL)

    def test_get_th_count(self):
        columns = self.driver.find_elements(*TABLE_COLUMN)

        self.assertEqual(3, len(columns))

    def test_get_tr_count(self):
        rows = self.driver.find_elements(*TABLE_ROW)

        self.assertEqual(6, len(rows))

    def test_get_progress_column(self):
        progress_column = self.driver.find_element(*PROGRESS_COLUMN)

        self.assertEqual("80%", progress_column.text)

    def test_get_completed_progress(self):
        completed_progress = self.driver.find_elements(*COMPLETED_PROGRESS)
        progresses = []

        for progress in completed_progress:
            progresses.append(progress.text)

        self.assertIn("100%", progresses)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
