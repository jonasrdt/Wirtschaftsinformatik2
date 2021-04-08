#################################################
# Webscraper to get movie informations from IMDb
# v.0.1.
# Jonas Reinhardt / FH Kiel
#################################################

# Do all the import stuff
import requests # will allow us to send HTTP requests to get HTML files
from requests import get 

from bs4 import BeautifulSoup # will help us parse the HTML files

import pandas as pd # will help us assemble the data into a DataFrame to clean and analyze it
import numpy as np

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
movie_div = soup.find_all('div', class_="lister-item mode-advanced")


# iterate through every div container stored in movie_div
for container in movie_div:

    name = container.h3.a.text
    titles.append(name)
