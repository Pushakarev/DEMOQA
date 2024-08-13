import time

from locators.alert_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NastedFramesPageLocators, ModalDialogsPageLocators
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
        text = 'Maxim'
        self.element_is_visable(self.locators.PROMPT_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_IMPUT).text

        return text, text_result

class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame (self,frame_num):
        if frame_num == "frame1":
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]

        if frame_num == "frame2":
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            return [text, width, height]


class NastedFramesPage(BasePage):
    locators = NastedFramesPageLocators()
    def checked_nested_drame(self):
        parent_frame= self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text= self.element_is_present(self.locators.PARENT_TEXT).text

        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXTX).text
        return parent_text, child_text

class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()


    def check_modal_dialogs(self):
        self.element_is_visable(self.locators.SMALL_BUTTON).click()
        title_small = self.element_is_visable(self.locators.TITLE_SMALL_MODAL).text
        body_small_text = self.element_is_visable(self.locators.BODY_SMALL).text
        self.element_is_visable(self.locators.CLOSE_SMALL_BUTTON).click()
        self.element_is_visable(self.locators.LARG_BUTTON).click()

        title_large = self.element_is_visable(self.locators.TITLE_LARGE_MODAL).text
        body_large_text = self.element_is_visable(self.locators.BODY_LARGE).text
        return [title_small, len(body_small_text)], [title_large,len(body_large_text)]






















