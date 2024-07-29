import random
import base64
import time
from pages.base_page import BasePage
from conftest import driver
import pytest
from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
import allure

#
#
# # базовые методы
# class BasePage:
#     def __init__(self, driver, url):
#         self.driver = driver
#         self.url = url
#
#
#
#     def open(self):
#         self.driver.get(self.url)
#
#     def element_is_visable(self, locator, timeout = 5):
#         return wait (self.driver,timeout).until(EC.visibility_of_element_located(locator))
#
#
#     def elements_are_visable(self, locator, timeout = 5):
#         return wait (self.driver,timeout).until(EC.visibility_of_all_elements_located(locator))
#
#
#
#     def element_is_present(self, locator, timeout = 5):
#         return wait (self.driver,timeout).until(EC.presence_of_element_located(locator))
#
#
#     def elements_are_present(self, locator, timeout = 5):
#         return wait (self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
#
#
#     def element_is_not_visable(self, locator, timeout = 5):
#         return wait (self.driver,timeout).until(EC.invisibility_of_element_located(locator))
#
#     def element_is_clickable(self, locator, timeout=5):
#         return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
#
#     def go_to_element(self, element):
#         self.driver.execute_script ("arguments[0].scrollIntoView();", element)
#
#     def action_double_click(self, element):
#         action = ActionChains(self.driver)
#         action.double_click(element)
#         action.perform()
#
#     def action_right_click(self,element):
#         action = ActionChains(self.driver)
#         action.context_click(element)
#         action.perform()
#
#
#







class TestElements:
    class TestTextBox:



        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()

            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()

            assert full_name == output_name
            assert email == output_email
            assert current_address == output_cur_addr
            assert permanent_address == output_per_addr

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button("yes")
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button("impressive")
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button("no")
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes'
            assert output_impressive == 'Impressive'
            assert output_no == 'No'

    class TestWebTable:
        def test_web_table_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_person(key_word)
            table_result = web_table_page.check_search_person()
            print(table_result)
            print(key_word)
            assert key_word in table_result

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            print(age)
            print(row)
            assert age in row

        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_delete_person()
            assert text == "No rows found"

        def test_web_tabl_change_row(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], ' Test Failed('

    class TestButtonPage:

        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')

            assert double == "You have done a double click"
            assert right == "You have done a right click"
            assert click == "You have done a dynamic click"

    class TestLinksPage:
        def test_check_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            href_link, current_url = links_page.check_new_tab()
            print(href_link)

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            response_code = links_page.check_broken_link("https://demoqa.com/bad-request")
            assert response_code == 400

    class TestUploadAndDownload:

        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_download_page.open()
            file_name,result =upload_download_page.upload_file()
            assert file_name== result


        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
            upload_download_page.open()
            upload_download_page.download_file()
            check = upload_download_page.download_file()
            assert check is True

    class TestDynamicPropertiesPage:

        def test_dynamic_properties(self,driver):
            dynamic_properties_page = DynamicPropertiesPage(driver,'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after= dynamic_properties_page.check_changed_color()
            assert color_before != color_after

        def test_appear_button (self,driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.checked_apper_of_button()
            assert appear is True






