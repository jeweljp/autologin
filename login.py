#!/usr/bin/python3
_author_ = "Jewel Jo Prince"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

#Download and extract geckodriver
with webdriver.Firefox(executable_path='Path/to/geckodriver') as driver:

#Enter the IP of login page
    my_login_page = "My IP"

#Enter your credentials here
    my_username = "Enter your username"
    my_password = "Enter my password"

#Enter the respective name tags
    username_tag = "Name tag of username field"
    password_tag = "Name tag of password field"
    submit_tag = "Name tag of submit button"

    wait = WebDriverWait(driver, 10)
    driver.get(my_login_page)
    driver.find_element_by_name(username_tag).send_keys(my_username)
    driver.find_element_by_name(password_tag).send_keys(my_password)
    driver.find_element_by_name(submit_tag).click()
    time.sleep(3)
