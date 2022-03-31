import unittest

from config import browser
from locators.calendar_locators import CALENDAR_URL, INPUT, DAYS


class CalendarPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(CALENDAR_URL)

    def test_pick_day(self):
        date_picker_input = self.driver.find_element(*INPUT)
        date_picker_input.click()

        selected_day = ""
        days = self.driver.find_elements(*DAYS)

        for day in days:
            if day.text == "10":
                selected_day = day

        selected_day.click()

        self.assertIn("10", date_picker_input.get_attribute("value"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
