import base64
import os
import random
import time

import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from locators.elements_page_locators import TextBoxPageLocator, RadioButtonLocators, WebTablePageLocators, \
    ButtonPageLocators, LinksPageLocators, UploadAndDownloadPageLocators, DynamicPropertiesPageLocators
from generator.generator import generated_person, generate_file
from locators.elements_page_locators import CheckBoxPageLocators
from generator.generator import generate_file
from pages.base_page import BasePage

# заполняем поля
class TextBoxPage(BasePage):
    locators = TextBoxPageLocator
# заполнить поля для ввода данных пользователя
    def fill_all_fields(self):
        person_generator = generated_person()
        person_info = next(person_generator)
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visable(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visable(self.locators.EMAIL).send_keys(email)
        self.element_is_visable(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visable(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visable(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address




        # проверяем заполненную форму
    def check_filled_form(self):
        full_name= self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address =self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address =self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return  full_name, email, current_address,permanent_address

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.get = None

    def open_full_list(self):
        self.element_is_visable(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visable(self.locators.ITEM_LIST)
        # for item in item_list:
        #     self.go_to_element(item)
        #     item.click()
        count = 21
        while count != 0:
            item = item_list [random.randint(1,14)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                print(item)
                count -=1
            else:
                break


    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
            print(data)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()



    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
            print(data)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators

    def click_on_the_radio_button(self, choice):
        choices = {
            'yes': self.locators.RADIO_BUTTON_YES,
            'impressive': self.locators.RADIO_BUTTON_IMPRESSIVE,
            'no': self.locators.RADIO_BUTTON_NO
        }
        self.element_is_visable(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators= WebTablePageLocators()


    def add_new_person (self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname= person_info.firstname
            lastname= person_info.lastname
            email =person_info.email
            salary= person_info.salary
            age =person_info.age
            department = person_info.department
            self.element_is_visable(self.locators.ADD_BUTTON).click()
            self.element_is_visable(self.locators.FIRST_INPUT).send_keys(firstname)
            self.element_is_visable(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visable(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visable(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visable(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visable(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visable(self.locators.SUBMIT).click()
            count-=1
            print(firstname, lastname, email, age, department, salary)
            return [firstname, lastname, str(age), email,str(salary),department]
    def  check_new_added_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data=[]
        for item in person_list:
            data.append(item.text.splitlines())
        return data

    def search_person(self,key_word):
        self.element_is_visable(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person (self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info =next(generated_person())
        age = person_info.age
        self.element_is_visable(self.locators.UPDATE_BUTTON).click()
        self.element_is_visable(self.locators.AGE_INPUT).clear()
        self.element_is_visable(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visable(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        self.element_is_visable(self.locators.DELETE_BUTTON).click()

    def check_delete_person(self):
        return self.element_is_present(self.locators.NOW_ROWS_FOUND).text

    def select_up_to_some_rows(self):
        count = [5,10,20,25,50,100]
        data = []
        for x in count:
            count_row_button =  self.go_to_element(self.element_is_visable(self.locators.COUNT_ROW_LIST))
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visable(By.CSS_SELECTOR,f'option[value="{x}"]').click()
            data.append(self.check_count_rows())



    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)



class ButtonPage(BasePage):
    locators = ButtonPageLocators()

    def click_on_different_button(self,type_click):
        if type_click == 'double':
            self.action_double_click(self.element_is_visable(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCESS_DOUBLE)


        if type_click == "right":
            self.action_right_click(self.element_is_visable(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCESS_RIGHT)


        if type_click == "click":
            self.element_is_visable(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCESS_CLICK_ME)


    def check_clicked_on_the_button(self,element):
        return self.element_is_present(element).text

class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab(self):
        simple_link = self.element_is_visable(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(f'{link_href}')
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url

        else:
            return  link_href, request.status_code


    def check_broken_link(self,url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code


class UploadAndDownloadPage (BasePage):
    locators = UploadAndDownloadPageLocators()

    def upload_file(self):
        file_name, path = generate_file()
        self.element_is_present(self.locators.UPLOAD).send_keys(path)
        os.remove(path)
        text= self.element_is_present(self.locators.UPLOADED_FILE).text
        return file_name.split("\\")[-1], text.split("\\")[-1]
        print(text)

    def download_file(self):
        link=self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute("href")
        link_b = base64.b64decode(link)
        path_name_file = rf'C:\INSTALL\filename{random.randint(0,99)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        return check_file




class DynamicPropertiesPage (BasePage):
    locators = DynamicPropertiesPageLocators()
    def check_changed_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGED_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    def checked_apper_of_button (self):
        try:
            self.element_is_visable(self.locators.VISIBLE_AFTER_5_SECONDS_BUTTON)

        except TimeoutException:
            return False
        return True




















































