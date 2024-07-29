import time

from locators.alert_page_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage (BasePage):
    locators = BrowserWindowsPageLocators()

    def check_open_new_tab(self):
        self.element_is_visable(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_open_new_window(self):
        self.element_is_visable(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visable(self.locators.SEE_ALERT_BUTTON).click()
        alert_window= self.driver.switch_to.alert
        return alert_window.text

    def check_see_alert_after_5seconds(self):
        self.element_is_visable(self.locators.APPER_ALERT_BUTTON).click()
        time.sleep(6)
        alert_window= self.driver.switch_to.alert
        return alert_window.text

    def check_see_alert_confirm(self):
        self.element_is_visable(self.locators.CONFIRM_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_see_alert_prompt(self):
        text = 'fdfdf'
        self.element_is_visable(self.locators.PROMPT_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_IMPUT).text

        return text, text_result






