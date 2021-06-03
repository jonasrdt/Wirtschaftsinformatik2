# Requests wird benötigt, um einen GET Request zu stellen
import requests
from requests import get

# Übersetzen der Website in Text
from bs4 import BeautifulSoup

# Zusammensetzen der Daten in DataFrames
import pandas as pd

# URL festlegen
url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"

# Variable in der das Ergebnis des GET Requests gespeichert wird
results = requests.get(url)

# Übersetzen der Inhalte in results
soup = BeautifulSoup(results.text, "html.parser")

# Initialisieren der Variablen für geforderte Inhalte
titel = []
jahr = []
dauer = []
umsatz = []
votes = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')

for container in movie_div:
    
    # Zwischenspeichern des Titels aus dem aktuellen Container
    titel_temp = container.h3.a.text
    # Speichern des Titels in die Liste aller Titel
    titel.append(titel_temp)

    # Zwischenspeichern des Jahres aus dem aktuellen Container
    jahr_temp = container.h3.find('span', class_="lister-item-year").text
    # Speichern des Jahres in die Liste aller Jahre
    jahr.append(jahr_temp)

    # Zwischenspeichern der Dauer aus dem aktuellen Container
    if container.find('span', class_="runtime"):
        dauer_temp = container.find('span', class_="runtime").text
    else:
        dauer_temp = ''
    # Speichern der Dauer in die Liste
    dauer.append(dauer_temp)

    nv = container.find_all('span', attrs={'name': 'nv'})

    # Zwischenspeichern der Votes aus dem aktuellen Container
    votes_temp = nv[0].text
    # Speichern der Votes in die Liste aller Votes
    votes.append(votes_temp)

    # Zwischenspeichern der Votes aus dem aktuellen Container
    if len(nv) > 1:
        umsatz_temp = nv[1].text
    else:
        umsatz_temp = ''
    # Speichern der Votes in die Liste aller Votes
    umsatz.append(umsatz_temp)

# Überführen der Listen in ein DataFrame mit entsprechenden Spaltentiteln
movies = pd.DataFrame({
    'Titel': titel,
    'Jahr': jahr,
    'Votes': votes,
    'Umsatz': umsatz,
    'Dauer': dauer
})

# Entfernen der Klammern um das Jahr herum
movies['Jahr'] = movies['Jahr'].str.extract('(\d+)').astype(int)
# Entfernen der Minuten hinter der Laufzeit
movies['Dauer'] = movies['Dauer'].str.extract('(\d+)').astype(int)
# Entfernen des $ und des M vor und nach dem Gesamtumsatz
movies['Umsatz'] = movies['Umsatz'].map(lambda x: x.lstrip('$').rstrip('M'))

print(movies)
movies.to_csv('movies2.csv')