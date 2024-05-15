# importation

import requests
from bs4 import BeautifulSoup

# Utilisation

url =  'https://www.google.fr'

# recuperer la page à scraper

response = requests.get(url)


# Parser le resultat en HTML pour l'exploitation

html_soup = BeautifulSoup(response.text, 'html.parser')


# Verifier que le scrapping à marché

print(response.status_code)
200 # tout va bien
