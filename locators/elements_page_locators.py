from selenium.webdriver.common.by import By


class TextBoxPageLocator:

# locators to main menu
    FULL_NAME = (By.CSS_SELECTOR, "input[id = 'userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id = 'userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id = 'currentAddress']")
    PERMANENT_ADDRESS =(By.CSS_SELECTOR, "textarea[id = 'permanentAddress']")
    SUBMIT =(By.CSS_SELECTOR, "button[id = 'submit']")
# locators to print page
    CREATED_FULL_NAME =(By.CSS_SELECTOR, "div[id='output'] p[id='name']")
    CREATED_EMAIL =(By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS =(By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS =(By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
 # локаторы к чек боксу
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title = 'Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class = 'rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class = 'rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

ALL_FILES= (By.CSS_SELECTOR, "li[class='rct-node rct-node-parent rct-node-expanded']")

class RadioButtonLocators:
    RADIO_BUTTON_YES =(By.CSS_SELECTOR,"label[class^='custom-control'][for='yesRadio']")
    RADIO_BUTTON_IMPRESSIVE = (By.CSS_SELECTOR,"label[class^='custom-control'][for='impressiveRadio']")
    RADIO_BUTTON_NO =(By.CSS_SELECTOR,"label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT =(By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablePageLocators:
    # add person
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id = 'addNewRecordButton']")
    FIRST_INPUT = (By.CSS_SELECTOR, "input[id= 'firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[id= 'lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id= 'userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id= 'age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id= 'salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id= 'department']")
    SUBMIT = (By.CSS_SELECTOR, "button[id = 'submit']")

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title ='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    NOW_ROWS_FOUND = (By.CSS_SELECTOR, "div[class ='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label ='rows per page']")

    # update
    UPDATE_BUTTON= (By.CSS_SELECTOR, "span[title= 'Edit']")

class ButtonPageLocators:
    DOUBLE_BUTTON = (By.ID, 'doubleClickBtn')
    RIGHT_CLICK_BUTTON = (By.ID, 'rightClickBtn')
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")

    # result
    SUCESS_DOUBLE= (By.ID,'doubleClickMessage')
    SUCESS_RIGHT= (By.ID,'rightClickMessage')
    SUCESS_CLICK_ME = (By.ID,'dynamicClickMessage')


class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id= 'simpleLink']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id= 'bad-request']")



class UploadAndDownloadPageLocators:
    UPLOAD = (By.CSS_SELECTOR, "input[id= 'uploadFile']")
    DOWNLOAD = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/a')
    UPLOADED_FILE = (By.CSS_SELECTOR, "p[id= 'uploadedFilePath']")
    DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id= 'downloadButton']")

class DynamicPropertiesPageLocators:
    COLOR_CHANGED_BUTTON = (By.CSS_SELECTOR, "button[id= 'colorChange']")
    VISIBLE_AFTER_5_SECONDS_BUTTON = (By.CSS_SELECTOR, "button[id= 'visibleAfter']")














