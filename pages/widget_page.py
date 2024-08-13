import random
import time
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from generator.generator import generated_color, generated_date
from locators.widget_page_locators import AcordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SlidePageLocators, ProgressBarPageLocators, TabPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SelectMenuPageLocators
from pages.base_page import BasePage

class AccordianPage(BasePage):

    locators= AcordianPageLocators()
    def check_accordian(self,accordian_num):
        accordian =  { 'first':
                           {'title': self.locators.FIRST_SECTION,
                            'content': self.locators.FIRST_SECTION_CONTENT},
                       'second':
                           {'title': self.locators.SECOND_SECTION,
                            'content': self.locators.SECOND_SECTION_CONTENT},
                       'third':
                            {'title': self.locators.THIRD_SECTION,
                             'content': self.locators.THIRD_SECTION_CONTENT},
                       }

        section_title = self.element_is_visable(accordian[accordian_num] ['title'])
        section_title.click()
        section_content = self.element_is_visable(accordian[accordian_num]['content']).text
        return [section_title.text,len(section_content)]

class AutoCompletePage(BasePage):
    locators= AutoCompletePageLocators()
    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=3)
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value(self):
        count_value_befor = len(self.elements_are_visable(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visable(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visable(self.locators.MULTI_VALUE))
        return count_value_befor, count_value_after


    def check_color(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors= []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color [0]

    def check_one_color(self):
        color= self.element_is_visable(self.locators.SINGLE_CONTAINER).text
        return color

class DatePickerPage(BasePage):
    locators= DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date= self.element_is_visable(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.select_date_by_text(self.locators.DATE_SELECT_MONTH,date.month)
        self.select_date_by_text(self.locators.DATE_SELECT_YEAR,date.year)
        self.select_date_item_list(self.locators.DATE_SELECT_DAY,date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after


    def select_date_time(self):
        date = next(generated_date())
        input_date= self.element_is_visable(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
        self.select_date_item_list(self.locators.DATE_AND_TIME_MONTH_LIST,date.month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
        self.select_date_item_list(self.locators.DATE_AND_TIME_YEAR_LIST,'2020')
        self.select_date_item_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after



    def select_date_by_text(self,element,value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def select_date_item_list(self,elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

class SliderPage(BasePage):
    locators= SlidePageLocators()
    def change_slider(self):
        value_before = self.element_is_visable(self.locators.SLIDER_VALUE).get_attribute('value')
        slider = self.element_is_visable(self.locators.INPUT_SLIDER)
        self.action_drag_drop(slider, 89, 0)
        value_after = self.element_is_visable(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after

class ProgressBarPage(BasePage):
    locators= ProgressBarPageLocators()
    def change_progressbar(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar = self.element_is_visable(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar.click()
        time.sleep(2)
        progress_bar.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabPage(BasePage):
    locators = TabPageLocators()
    def check_tabs(self):
        what_button = self.element_is_visable(self.locators.TABS_WHAT)
        origin_button = self.element_is_visable(self.locators.TABS_ORIGIN)
        use_button = self.element_is_visable(self.locators.TAB_USE)
        more_button = self.element_is_visable(self.locators.TABS_MORE)
        what_button.click()
        what_content= self.element_is_visable(self.locators.TABS_WHAT_CONTENT).text
        origin_button.click()
        origin_content = self.element_is_visable(self.locators.TABS_ORIGIN_CONTENT).text
        use_button.click()
        use_content = self.element_is_visable(self.locators.TAB_USE_CONTENT).text
        return len(what_content), len(origin_content), len(use_content)

class ToolTipsPage(BasePage):
    locators= ToolTipsPageLocators()
    def get_text_from_too_tips(self,hover_elem, wait_elem):
        element =self.element_is_present(hover_elem)
        self.action_move(element)
        self.element_is_visable(wait_elem)
        tip_tool =self.element_is_visable(self.locators.TOOL_TIP_INNER)
        text =tip_tool.text
        return text

    def check_tool_tip (self):
        tool_tip_text = self.get_text_from_too_tips(self.locators.TOOL_TIP_BUTTON,self.locators.TOOL_TIP_BUTTON_SHADDOW)
        tool_tip_field = self.get_text_from_too_tips(self.locators.TOOL_TIP_FIELD,self.locators.TOOL_TIP_FIELD_SHADOW)
        tool_tip_contrary = self.get_text_from_too_tips(self.locators.CONTRARY_LINK,self.locators.CONTRARY_SHADOW)
        tool_tip_section  = self.get_text_from_too_tips(self.locators.SECTION_LINK,self.locators.SECTION_SHADOW)
        return tool_tip_text,tool_tip_field, tool_tip_contrary,tool_tip_section


class MenuPage(BasePage):
    locators =MenuPageLocators()
    def check_menu (self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM)
        data =[]
        for item in menu_item_list:
            self.action_move(item)
            data.append(item.text)
        return data


class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()
    def check_seleckt_value(self):
        select = self.element_is_present(self.locators.SELECT_COLOR)
        value_before =  Select(select).first_selected_option.text
        select.click()
        select = Select(select)
        select.select_by_index(5)
        value_after = select.first_selected_option.text
        return value_before, value_after






















