
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

user = input("Bitte geben Sie den Vornamen ein: ")
user.strip() # Entfernen von überflüssigen Leerzeichen links u. rechts

date = input("Bitte geben Sie das Geburtsdatum ein: ")
date.strip() # Entfernen von überflüssigen Leerzeichen links u. rechts

email = input("Bitte geben Sie Ihre E-Mail Adresse ein: ")
email.strip() # Entfernen von überflüssigen Leerzeichen links u. rechts


# Find webdriver for Chrome
browser = webdriver.Chrome(
    executable_path= chromedriver)

# Aufrufen der Website mithilfe von Selenium 
browser.get(url)

# Namen einfügen
try:
    user_input = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/input")
        )
    )
finally:
    user_input.send_keys(user)

# Namen einfügen
try:
    birthday_input = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div/div/div[3]/div[1]/div[3]/div[2]/div/div[1]/div/input")
        )
    )
finally:
    birthday_input.send_keys(date)

# Anklicken der Impfauswahl
try:
    erste_impfe = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div/div/div[3]/div[1]/div[8]/div[2]/div/div[1]")
        )
    )
finally:
    browser.implicitly_wait(10)
    erste_impfe.click()


# Email einfügen
try:
    email_input = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div/div/div[3]/div[2]/div[2]/div[1]/div/input")
        )
    )
finally:
    email_input.send_keys(email)


# Bestätigen der Eingabe
try:
    submit = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div/div/div[3]/div[4]/button")
        )
    )
finally:
    browser.implicitly_wait(10)
    submit.click()
