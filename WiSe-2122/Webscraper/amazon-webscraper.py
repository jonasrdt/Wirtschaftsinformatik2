# Requests wird benötigt, um einen GET Request zu stellen
import requests
from requests import get

# Übersetzung der Website in Text
from bs4 import BeautifulSoup 

# Zusammensetzen der Daten in DataFrames
import pandas as pd

# Übernehmen der URL von Amazon
url = "https://www.amazon.de/s?k=macbook+pro&__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"

# Forcieren der englischen Website
headers = {"Accept Language": "en-US, en; q=0.5"}

# Variable in der das Ergebnis des GET Requests gespeichert wird
results = requests.get(url, headers = headers)

# Übersetzen des Inhalts von result
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
    if container.find('span', class_='a-size-medium a-color-base a-text-normal'):
        titel_temp = container.find('span', class_='a-size-medium a-color-base a-text-normal').text
        titel.append(titel_temp)
    else:
        titel.append('')
        
    if container.find('span', class_='a-price-whole'):
        preis_temp = container.find('span', class_='a-price-whole').text
        preis.append(preis_temp)    
    else:
        preis.append('')
    
    if container.find('span', class_="a-icon-alt"):
        bewertung_temp = container.find('span', class_="a-icon-alt").text
        bewertung.append(bewertung_temp[:3])
    else:
        bewertung.append('')
  
  
produkte = pd.DataFrame({
    'Name': titel,
    'Preis': preis,
    'Bewertung': bewertung
})

produkte.to_csv('produkte.csv')
