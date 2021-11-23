# Requests wird benötigt, um einen GET Request zu stellen
import requests
from requests import get

# Übersetzung der Website in Text
from bs4 import BeautifulSoup 

# Zusammensetzen der Daten in DataFrames
import pandas as pd

# Forcieren der englischen Website
headers = {"Accept Language": "en-US, en; q=0.5"}

# URL festlegen
url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"

# Variable in der das Ergebnis des GET Requests gespeichert wird
results = requests.get(url, headers = headers)

# Übersetzen des Inhalts von result
soup = BeautifulSoup(results.text, "html.parser")

# Initialisieren der Variablen für die geforderten Inhalte
titel = []
jahr = []
dauer = []
imdb_rating = []
metascores = []
votes = []
umsatz = []

# Separieren der benötigten Informationen aus dem gesamten Code heraus
movie_div = soup.find_all('div', class_='lister-item mode-advanced')

for container in movie_div:
    
    # Zwischenspeichern des Titels aus dem aktuellen Container
    titel_temp = container.h3.a.text
    # Speichern des Titels in die Liste aller Titel
    titel.append(titel_temp)

    # Zwischenspeichern des Jahres aus dem aktuellen Container
    jahr_temp = container.h3.find('span', class_='lister-item-year').text
    # Speichern des Jahres in die Liste aller Jahres
    jahr.append(jahr_temp)

    # Zwischenspeichern der Dauer aus dem aktuellen Container
    dauer_temp = container.find('span', class_="runtime").text if container.p.find('span', class_='runtime') else ''
    # Speichern der Dauer in die Liste aller Dauern
    dauer.append(dauer_temp)

    # Raussuchen der NV Elemente
    nv = container.find_all('span', attrs={'name': 'nv'})

    # Zwischenspeichern der Votes aus dem aktuellen Container
    votes_temp = nv[0].text
    # Speichern der Votes in die Liste aller Votes
    votes.append(votes_temp)

    # Zwischenspeichern des Umsatzes aus dem aktuellen Container
    if len(nv) > 1:
        umsatz_temp = nv[1].text
    else:
        umsatz_temp = ''
    # Speichern des Umsatzes in die Liste aller Umsätze
    umsatz.append(umsatz_temp)
        
# Erstellen des DataFrames aus den bestehenden Listen
movies = pd.DataFrame({
    'Titel': titel,
    'Jahr': jahr,
    'Votes': votes,
    'Umsatz': umsatz,
    'Dauer (min)': dauer
})

# Entfernen der Klammern um das Jahr herum und Typumwandlung
movies['Jahr'] = movies['Jahr'].str.extract('(\d+)').astype(int)
# Entfernern des $ und des M aus der Umsatzspalte
movies['Umsatz'] = movies['Umsatz'].map(lambda x: x.lstrip('$').rstrip('M'))
# Bereinigen der Dauer um das Suffix "min" und Typumwandlung
movies['Dauer (min)'] = movies['Dauer (min)'].str.extract('(\d+)').astype(int)

# Exportieren des movie DataFrames in eine CSV
movies.to_csv('movies.csv')