from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set URL to interact with
url = 'https://modulanmeldung.fh-kiel.de/'

# Find webdriver for Chrome
browser = webdriver.Chrome(
    executable_path='') # Hinzufügen des chromedriver executable paths

# Aufrufen der Website mithilfe von Selenium 
browser.get(url)

# Wait until the "Anmelden" field is loaded and fully available to our script
try:
    login_button = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
            (By.XPATH, "/html/body/nav/div/div[2]/ul[2]/li[2]/form/button")
        )
    )
finally:
    browser.implicitly_wait(10)
    login_button.click()


pw = input("Bitte geben Sie Ihr Passwort ein: ")
pw.strip()

# E-Mail Adresse einfügen
try:
    user_input = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/div/section/form/div[1]/div/input")
        )
    )
finally:
    user_input.send_keys(user)

# Passwort einfügen
try:
    pw_input = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/div/section/form/div[2]/div/input")
        )
    )
finally:
    pw_input.send_keys(pw)