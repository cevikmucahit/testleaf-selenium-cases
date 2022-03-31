import unittest

from config import browser
from locators.frame_locators import FRAME_URL, FRAME, FRAME_IN_1, FRAME_IN_2, FRAMES, CLICK_FRAME, CLICK_FRAME_2, \
    MAIN_FRAME


class FramePage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(FRAME_URL)

    def test_click_frame(self):
        self.driver.switch_to.frame(self.driver.find_element(*FRAME))

        click_frame = self.driver.find_element(*CLICK_FRAME)
        click_frame.click()

        self.assertIn("Hurray", click_frame.text)

    def test_frame_in_frame(self):
        self.driver.switch_to.frame(self.driver.find_element(*FRAME_IN_1))
        self.driver.switch_to.frame(self.driver.find_element(*FRAME_IN_2))

        frame_button = self.driver.find_element(*CLICK_FRAME_2)
        frame_button.click()

        self.assertIn("Hurray! You Clicked Me.", frame_button.text)

    def test_get_frame_count(self):
        count = 1
        self.driver.switch_to.frame(self.driver.find_element(*MAIN_FRAME))

        frames = self.driver.find_elements(*FRAMES)

        for _ in frames:
            count = count + 1

        self.assertEqual(2, count)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
