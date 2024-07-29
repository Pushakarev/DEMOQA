import time
from conftest import driver
from pages.alert_page import BrowserWindowsPage, AlertsPage


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




