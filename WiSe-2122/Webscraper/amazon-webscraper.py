# Requests wird benötigt, um einen GET Request zu stellen
import requests
from requests import get

# Übersetzung der Website in Text
from bs4 import BeautifulSoup

# Zusammensetzen der Daten in DataFrames
import pandas as pd

# Übernehmen der URL von Amazon
url = "https://www.amazon.de/s?k=ipad&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2ZKMTZ2F0NLHQ&sprefix=ipad%2Caps%2C214&ref=nb_sb_noss_1"

# Forcieren der englischen Website
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

# Variable in der das Ergebnis des GET Requests gespeichert wird
results = requests.get(url, headers = HEADERS)

# # Übersetzen des Inhalts von result
soup = BeautifulSoup(results.text, "html.parser")


# Initialisieren der Variablen für die geforderten Inhalte
titel = []
bewertung = []
preis = []
preis_alt = []
versandart = []
displaygroesse = []
cpu = []
ram = []

# Separieren der benötigten Informationen aus dem gesamten Code heraus
item_div = soup.find_all('div', class_='sg-col-inner')

for container in item_div:
    # Namen einlesen
    if container.find('span', class_='a-size-medium a-color-base a-text-normal'):
        titel_temp = container.find('span', class_='a-size-medium a-color-base a-text-normal').text
        titel.append(titel_temp)
    else:
        titel.append('')

    # Preis einlesen
    if container.find('span', class_='a-price-whole'):
        preis_temp = container.find('span', class_='a-price-whole').text
        preis.append(preis_temp)    
    else:
        preis.append('')
    
    # Bewertung einlesen und slicen
    if container.find('span', class_="a-icon-alt"):
        bewertung_temp = container.find('span', class_="a-icon-alt").text
        # 4,8 von 5 Sternen
        bewertung.append(bewertung_temp[:3])
    else:
        bewertung.append('')

    for attribut in container.select('div.sg-col-inner > span.a-text-bold'):
        print("Ein Attribut lautet:", attribut.text)
        attribut_temp = str(attribut.text)
        if attribut_temp.find("Zoll") >= 0:
            displaygroesse.append(attribut_temp)
        elif attribut_temp.find("GHz") >= 0:
            cpu.append(attribut_temp)
        elif attribut_temp.find("GB") >= 0:
            ram.append(attribut_temp)
        else:
            displaygroesse.append(" ")
            cpu.append(" ")
            ram.append(" ")
  


produkte = pd.DataFrame({
    'Name': titel,
    'Preis': preis,
    'Bewertung': bewertung
})
print(produkte)
produkte.to_csv('produkte.csv')
produkte.to_excel('produkte.xls')