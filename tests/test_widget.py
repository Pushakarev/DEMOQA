import time

from conftest import driver

from pages.widget_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


class TestWidget:
    class TestAccordianPage:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0

    class TestAutoCompletePage:

        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color()
            assert colors == colors_result

        def test_remove_value(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_befor, count_value_after = autocomplete_page.remove_value()
            assert count_value_befor > count_value_after

        def test_fill_single(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_single()
            colors_result = autocomplete_page.check_one_color()
            assert color == colors_result

    class TestDatePage:

        def test_change_date(self, driver):
            date_picker = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker.open()
            value_date_before, value_date_after = date_picker.select_date()
            assert value_date_before != value_date_after

        def test_change_date_time(self, driver):
            date_picker = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker.open()
            value_date_before, value_date_after = date_picker.select_date_time()
            assert value_date_before != value_date_after

    class TestSliderPage:
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            value_before, value_after = slider.change_slider()
            assert value_before != value_after

    class TestProgressBarPage:

        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            value_before, value_after = progress_bar.change_progressbar()
            assert value_before != value_after

    class TestTabPAge:

        def test_tabs(self, driver):
            tabs = TabPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_content, origin_content, use_content = tabs.check_tabs()
            assert what_content != 0
            assert origin_content != 0
            assert use_content != 0

    class TestToolTips:

        def test_tool_tips(self, driver):
            tool = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool.open()
            tool_tip_text, tool_tip_field, tool_tip_contrary, tool_tip_section = tool.check_tool_tip()
            assert tool_tip_text == "You hovered over the Button"
            assert tool_tip_field == "You hovered over the Button"
            assert tool_tip_contrary == "You hovered over the text field"
            assert tool_tip_section == "You hovered over the Contrary"

    class TestMenuPage:
        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data = menu_page.check_menu()
            assert data== ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']

    class TestSelectMenuPage:

        def test_select_value(self,driver):
            select_value = SelectMenuPage(driver,'https://demoqa.com/select-menu')
            select_value.open()
            value_before, value_after=  select_value.check_seleckt_value()
            assert value_before != value_after


