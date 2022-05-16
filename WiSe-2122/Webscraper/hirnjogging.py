
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
url = 'https://www.brain-fit.com/html/reaktionstest.html'


# Find webdriver for Chrome
browser = webdriver.Chrome(
    executable_path= chromedriver)

# Aufrufen der Website mithilfe von Selenium 
browser.get(url)



# Anklicken der Impfauswahl
try:
    start = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/div/div/div/section[1]/div/div[1]/center/input")
        )
    )
finally:
    start.click()
    
    
# Anklicken der Impfauswahl
try:
    stop = WebDriverWait(browser, 120, 1).until(
        expect.element_to_be_clickable(
        (By.XPATH, "//input[@value='Stopp]")
        )
    )
finally:
    stop.click()