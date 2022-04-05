import unittest

from config import browser
from locators.checkbox_locators import CHEKCBOX_URL, CHECKED_CHECKBOX, VB_CHECKBOX, C_CHECKBOX, DESELECT_CHECKBOX, \
    ALl_CHECKBOX


class CheckboxPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(CHEKCBOX_URL)

    def test_select_checkbox(self):
        vb_checkbox = self.driver.find_element(*VB_CHECKBOX)
        c_checkbox = self.driver.find_element(*C_CHECKBOX)
        vb_checkbox.click()
        c_checkbox.click()

        self.assertTrue(vb_checkbox.get_attribute("checked") and c_checkbox.get_attribute("checked"))

    def test_checked_checkbox(self):
        checkbox = self.driver.find_element(*CHECKED_CHECKBOX)

        self.assertTrue(checkbox.get_attribute("checked"))

    def test_deselect_checkbox(self):
        checkbox = self.driver.find_element(*DESELECT_CHECKBOX)

        self.assertFalse(checkbox.get_attribute("checked"))

    def test_all_select_checkbox(self):
        checkboxes = self.driver.find_elements(*ALl_CHECKBOX)
        is_all_checked = []

        for checkbox in checkboxes:
            checkbox.click()
            is_all_checked.append(checkbox.get_attribute("checked"))

        self.assertNotIn(None, is_all_checked)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
