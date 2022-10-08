import requests
from bs4 import BeautifulSoup
import time

alllinks =  []
for i in range(4):
    url = "https://www.emploi.tg/recherche-jobs-togo?page=" + str(i)

    response = requests.get(url)
    if response.ok:
        last = BeautifulSoup(response.text, 'html.parser')
        links = last.select('a[href*="offre-emploi-togo"]') #Jobs Links on pages
        for x in links:
            y = x['href'] #Get value of attrib 'href'
            alllinks.append("https://www.emploi.tg" + y)
        alllinks_ = set(alllinks) # list -> set
        alllinks = list(alllinks_) # set -> list
        time.sleep(3)

#Write all Links in .txt file
with open('WaJobsLinks.txt', 'w') as file:
    for link in alllinks:
        file.write(link + '\n')


