# # import sys
# # import os
# # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#
# import pytest
# from selenium import webdriver
#
#
# @pytest.fixture(scope='function')
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service




@pytest.fixture(scope='function')
def driver():
    # Указываем полный путь к уже установленному ChromeDriver
    service = Service("C:\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()