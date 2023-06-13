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
url = 'https://ticket.impfen-sh.de/sh/start/termine'

# Find webdriver for Chrome
browser = webdriver.Chrome(
    executable_path= chromedriver)

# Aufrufen der Website mithilfe von Selenium 
browser.get(url)

user = input("Bitte geben Sie den Vornamen ein: ")
user.strip()

date = input("Bitte geben Sie das Geburtsdatum ein: ")
date.strip()

# Namen einfügen
try:
    user_input = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/input")
        )
    )
finally:
    user_input.send_keys(user)

# Geburtstag einfügen
try:
    date_input = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div/div/div[3]/div[1]/div[3]/div[2]/div/div[1]/div/input")
        )
    )
finally:
    date_input.send_keys(date)


art_der_impfung = input("Welche Impfung wollen Sie haben: \n 1. Impfung, Impfstoff Moderna, zugelassen ab 12 Jahren, STIKO empfiehlt ab 30 Jahren. \n 2. Impfung, Impfstoff Moderna, zugelassen ab 12 Jahren, STIKO empfiehlt ab 30 Jahren. \n Impfung, Auffrischimpfung, für Personen von 18 Jahren oder älter, Impfstoff Moderna, STIKO empfiehlt ab 30 Jahren.: ")
if art_der_impfung == "1":
    # Klicken des ersten Buttons
    try:
        erste_impfe = WebDriverWait(browser, 120, 1).until(
            expect.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div/div/div[3]/div[1]/div[4]/div[2]/div/div[1]/div")
            )
        )
    finally:
        browser.implicitly_wait(10)
        erste_impfe.click()
elif art_der_impfung == "2":
# Klicken des zweiten Buttons
    try:
        zweite_impfe = WebDriverWait(browser, 120, 1).until(
            expect.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div/div/div[3]/div[1]/div[5]/div[2]/div/div[1]/div")
            )
        )
    finally:
        browser.implicitly_wait(10)
        zweite_impfe.click()   
elif art_der_impfung == "3":
# Klicken des zweiten Buttons
    try:
        dritte_impfe = WebDriverWait(browser, 120, 1).until(
            expect.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div/div/div[3]/div[1]/div[6]/div[2]/div/div[1]/div")
            )
        )
    finally:
        browser.implicitly_wait(10)
        dritte_impfe.click()

email = input("Bitte geben Sie Ihre E-Mail Adresse ein: ")
# E-Mail einfügen
try:
    mail_input = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div/div/div[3]/div[2]/div[2]/div[1]/div/input")
        )
    )
finally:
    mail_input.send_keys(email)

# Klicken des Bestätigen Buttons
try:
    confirm = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div/div/div[3]/div[4]/button")
        )
    )
finally:
    browser.implicitly_wait(10)
    confirm.click()