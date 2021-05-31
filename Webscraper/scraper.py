#################################################
# Webscraper to get movie informations from IMDb
#################################################

# Do all the import stuff
import requests # will allow us to send HTTP requests to get HTML files
from requests import get 

from bs4 import BeautifulSoup # will help us parse the HTML files

import pandas as pd # will help us assemble the data into a DataFrame to clean and analyze it


# Since we may have a different language, we want to commit on english
headers = {"Accept Language": "en-US, en;q=0.5"}

# Define the URL we want to access
url = "https://imdb.com/search/title/?groups=top_1000&ref_=adv_prv"

# Variable in which we store the results of the request.get results
results = requests.get(url, headers = headers)

# Make the content we grabbed easy to read by using BeautifulSoup
# the variable we create to assign the method BeatifulSoup to, which specifies a desired format of results using the HTML parser
# this allows Python to read the components of the page rather than treating it as one long string
soup = BeautifulSoup(results.text, "html.parser")

# print what we’ve grabbed in a more structured tree format, making it easier to read
# print(soup.prettify())

# Initialize empty lists to store the data we fetched
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

# tell our scraper to find all of these lister-item mode-advanced divs
# movie_div is the variable we’ll use to store all of the div containers with a class of lister-item mode-advanced
# the find_all() method extracts all the div containers that have a class attribute of lister-item mode-advanced from what we have stored in our variable soup
movie_div = soup.find_all('div', class_='lister-item mode-advanced')

# print(movie_div)


# iterate through every div container stored in movie_div
for container in movie_div:

    # Store the title data found in the div
    name = container.h3.a.text
    # Aftwards store the data in the titles list
    titles.append(name)

    # Since the span tag in this case is the second span tag we want go grab, we need a different method
    year = container.h3.find('span', class_='lister-item-year').text
    years.append(year)

    # Find the runtime and define a case if it is not existent
    runtime = container.find('span', class_='runtime').text if container.p.find('span', class_='runtime') else ''
    time.append(runtime)

    # Find the IMDb rating
    imdb = float(container.strong.text)
    imdb_ratings.append(imdb)

    #metascore
    m_score = container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-'
    metascores.append(m_score)

    #there are two NV containers, grab both of them as they hold both the votes and the grosses
    nv = container.find_all('span', attrs={'name': 'nv'})
        
    #filter nv for votes
    vote = nv[0].text
    votes.append(vote)
        
    #filter nv for gross
    grosses = nv[1].text if len(nv) > 1 else '-'
    us_gross.append(grosses)

# Put the scraped data in the pandas dataframe and give it fitting names
movies = pd.DataFrame({
    'Titel': titles,
    'Jahr': years,
    'Dauer': time,
    'IMDb Rating': imdb_ratings,
    'Metascore': metascores,
    'Votes': votes,
    'us_grossMillions': us_gross
})

# Let's see how the result looks so far
print(movies)

# Remove parantheses from the year data
movies['Jahr'] = movies['Jahr'].str.extract('(\d+)').astype(int)
movies['Dauer'] = movies['Dauer'].str.extract('(\d+)').astype(int)


# Remove the commas from the votes and convert the it to integer
movies['Votes'] = movies['Votes'].str.replace(',', '').astype(int)

# Cleaning the us_grossMillions column
movies['us_grossMillions'] = movies['us_grossMillions'].map(lambda x: x.lstrip('$').rstrip('M'))
movies['us_grossMillions'] = pd.to_numeric(movies['us_grossMillions'], errors = 'coerce')

# Extract csv-File
movies.to_csv('movies.csv')