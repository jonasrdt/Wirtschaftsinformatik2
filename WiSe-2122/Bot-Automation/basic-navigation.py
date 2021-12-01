from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set URL to interact with
url = ''

# Find webdriver for Chrome
browser = webdriver.Chrome(
    executable_path='')

# Aufrufen der Website mithilfe von Selenium 
browser.get(course)


