import requests
from bs4 import BeautifulSoup
import time
url = "https://www.emploi.tg/"
response = requests.get(url)

latestlks = []

if response.ok:
    last = BeautifulSoup(response.text, 'html.parser')
    links = last.select('a[href*=".tg/offre-emploi-togo"]') #Latest Jobs Links on homePage
    for x in links:
        y = x['href'] #Get value of attrib 'href'
        latestlks.append(y)
    latestlks_ = set(latestlks) # list -> set
    latestlks = list(latestlks_) # set -> list
    print(latestlks)

# Write all Links in .txt file
with open('top_jobs.txt', 'w') as file:
    for link in latestlks:
        file.write(link + '\n')