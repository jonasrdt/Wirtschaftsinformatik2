# 1. Herunterladen von Google Chrome https://www.google.com/intl/de/chrome/ 
# 2. Google Chrome Version herausfinden 
# 3. Passende Chromedriver herunterladen https://chromedriver.chromium.org/downloads
# 4. Selenium installieren
#   Windows: py -m pip install selenium
#   MacOS: python3 -m pip install selenium
# 5. Ausführen

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

# aktuelles Verzeichnis der Datei
aktVerzeichnis = os.path.dirname(__file__)

# Zusammensetzen des Verzeichnispfads zum chromedriver
chromedriver = os.path.join(aktVerzeichnis, 'chromedriver')

# Set URL to interact with
url = 'https://www.foerde-sparkasse.de/de/home.html'

# Find webdriver for Chrome
browser = webdriver.Chrome(
    executable_path= chromedriver)

# Aufrufen der Website mithilfe von Selenium 
browser.get(url)

# Wait until the "Anmelden" field is loaded and fully available to our script
try:
    login_button = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div[2]/div/div[4]/form/button")
        )
    )
finally:
    browser.implicitly_wait(10)
    login_button.click()

user = input("Bitte geben Sie Ihre E-Mail Adresse ein: ")
user.strip()

pw = input("Bitte geben Sie Ihr Passwort ein: ")
pw.strip()

for i in range(250):
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

    # Click the button "Anmelden"
    try:
        login_button_2 = WebDriverWait(browser, 120, 1).until(
            expect.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div/div/section/form/div[4]/div/input")
            )
        )
    finally:
        browser.implicitly_wait(10)
        login_button_2.click()
        
