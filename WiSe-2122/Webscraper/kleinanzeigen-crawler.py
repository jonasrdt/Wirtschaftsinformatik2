# Requests wird benötigt, um einen GET Request zu stellen
import requests
from requests import get

# Übersetzung der Website in Text
from bs4 import BeautifulSoup

# Zusammensetzen der Daten in DataFrames
import pandas as pd

# Übernehmen der URL von Amazon
url = "https://www.ebay-kleinanzeigen.de/s-kiel/surfbretter/k0l663r50"

# Vorgaukeln eines "echten" Browsern
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2228.0 Safari/537.36',
            'Accept-Language': 'de-DE, en;q=0.5'})


# Variable in der das Ergebnis des GET Requests gespeichert wird
results = requests.get(url, headers = HEADERS)

# # Übersetzen des Inhalts von result
soup = BeautifulSoup(results.text, "html.parser")

# Definieren der Inhalte, die wir speichern wollen
titel = [] # Leeres Listenelement
standort = []
einstellungsdatum = []
beschreibung = []
preis = []
versandart = []

# Separieren der benötigten Informationen aus dem gesamten Code heraus
item_div = soup.find_all('div', class_='aditem-main')

for artikel in item_div:
    # Namen einlesen
    if artikel.find('a', class_='ellipsis'):
        titel_temp = artikel.find('a', class_='ellipsis').text
        titel.append(titel_temp)
    else:
        titel.append('')

print(titel)
