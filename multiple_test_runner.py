import unittest

from alert import AlertPage
from appear import AppearPage
from autocompletes import AutoCompletePage
from buttons import ButtonsPage
from calendars import CalendarPage
from checkbox import CheckboxPage
from disappear import DisappearPage
from download import DownloadPage
from draggables import DraggablePage
from dropdowns import DropdownPage
from droppables import DroppablePage
from edits import EditsPage
from frame import FramePage
from hyperlinks import HyperlinksPage
from images import ImagePage
from radio_button import RadioButtonPage
from selectable import SelectablePage
from sortables import SortablePage
from table import TablePage
from tooltip import TooltipPage
from upload import UploadPage
from wait_for_alert import WaitalertPage
from wait_for_text_change import TextchangePage
from window import WindowPage

buttons_cases = unittest.TestLoader().loadTestsFromTestCase(ButtonsPage)
edits_cases = unittest.TestLoader().loadTestsFromTestCase(EditsPage)
alerts_cases = unittest.TestLoader().loadTestsFromTestCase(AlertPage)
appears_cases = unittest.TestLoader().loadTestsFromTestCase(AppearPage)
autocompletes_cases = unittest.TestLoader().loadTestsFromTestCase(AutoCompletePage)
calendars_cases = unittest.TestLoader().loadTestsFromTestCase(CalendarPage)
checkbox_cases = unittest.TestLoader().loadTestsFromTestCase(CheckboxPage)
disappear_cases = unittest.TestLoader().loadTestsFromTestCase(DisappearPage)
download_cases = unittest.TestLoader().loadTestsFromTestCase(DownloadPage)
draggable_cases = unittest.TestLoader().loadTestsFromTestCase(DraggablePage)
dropdown_cases = unittest.TestLoader().loadTestsFromTestCase(DropdownPage)
droppable_cases = unittest.TestLoader().loadTestsFromTestCase(DroppablePage)
frame_cases = unittest.TestLoader().loadTestsFromTestCase(FramePage)
hyperlink_cases = unittest.TestLoader().loadTestsFromTestCase(HyperlinksPage)
image_cases = unittest.TestLoader().loadTestsFromTestCase(ImagePage)
radiobutton_cases = unittest.TestLoader().loadTestsFromTestCase(RadioButtonPage)
selectable_cases = unittest.TestLoader().loadTestsFromTestCase(SelectablePage)
sortables_cases = unittest.TestLoader().loadTestsFromTestCase(SortablePage)
table_cases = unittest.TestLoader().loadTestsFromTestCase(TablePage)
tooltip_cases = unittest.TestLoader().loadTestsFromTestCase(TooltipPage)
upload_cases = unittest.TestLoader().loadTestsFromTestCase(UploadPage)
wait_for_alert_cases = unittest.TestLoader().loadTestsFromTestCase(WaitalertPage)
wait_for_text_change_cases = unittest.TestLoader().loadTestsFromTestCase(TextchangePage)
window_cases = unittest.TestLoader().loadTestsFromTestCase(WindowPage)

test_suite = unittest.TestSuite(
    [alerts_cases, appears_cases, autocompletes_cases, buttons_cases, calendars_cases, checkbox_cases,
     disappear_cases, download_cases, draggable_cases, dropdown_cases, droppable_cases, edits_cases, frame_cases,
     hyperlink_cases, image_cases, radiobutton_cases, selectable_cases, sortables_cases, table_cases, tooltip_cases,
     upload_cases, wait_for_alert_cases, wait_for_text_change_cases, window_cases])

unittest.TextTestRunner(verbosity=2).run(test_suite)
