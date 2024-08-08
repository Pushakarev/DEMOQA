import time
from conftest import driver
from pages.alert_page import BrowserWindowsPage, AlertsPage, FramesPage, NastedFramesPage, ModalDialogsPage


class TestAlertsFrameWindow:
    class TestBrowserWindows:

        def test_new_tab(self,driver):
            new_tab_page= BrowserWindowsPage (driver,'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_open_new_tab()
            assert text_result == 'This is a sample page'




        def test_new_window(self,driver):
            new_window_page= BrowserWindowsPage (driver,'https://demoqa.com/browser-windows')
            new_window_page.open()
            text_result = new_window_page.check_open_new_tab()
            assert text_result == 'This is a sample page'

    class TestAlertPage:

        def test_see_alert(self,driver):
           alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
           alert_page.open()
           alert_text= alert_page.check_see_alert()
           assert alert_text == 'You clicked a button'

        def test_see_alert_after_5seconds(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert_after_5seconds()
            assert alert_text == 'This alert appeared after 5 seconds'

        def test_see_alert_confirm(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert_confirm()
            assert alert_text == 'Do you confirm action?'

        def test_see_alert_prompt(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_see_alert_prompt()
            assert alert_text == f'You entered {text}'

    class TestFramesPage:

        def test_frames(self,driver):
            frame_page = FramesPage(driver,'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame2 == ['This is a sample page', '100px', '100px']
            assert result_frame1 == ['This is a sample page', '500px', '350px']

    class TestNestedFramesPage:

        def test_nested_frames(self, driver):
            nasted_frame_page = NastedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nasted_frame_page.open()
            parent_text, child_text= nasted_frame_page.checked_nested_drame()
            assert parent_text== 'Parent frame'
            assert  child_text == 'Child Iframe'

    class TestModalDialogsPage:

        def test_modal_dialogs(self,driver):

            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small, large= modal_dialogs_page.check_modal_dialogs()
            assert small[1] < large[1]
            assert small [0] =='Small Modal'
            assert large [0] == 'Large Modal'















