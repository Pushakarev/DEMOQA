import time
from conftest import driver
from pages.alert_page import BrowserWindowsPage


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
