# Part One : Scraping
import requests
from bs4 import BeautifulSoup
import sqlite3
import time
from datetime import date

#source = 'https://www.pharmacie.tg/
source =  "" 
pharmacies = []

if source:
    url = source.strip()
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        t_nom = soup.find('div', {'class': 'bloc-title'}) 
        nom = t_nom.text.strip()

        t_tel = soup.find('div', {'class': 'bloc-title'})
        tel = t_tel.text.strip()

        t_Qt = soup.find('div', {'class': 'bloc-title'})
        Qt = t_Qt.text.strip()

        t_ville_pays = soup.find('div', {'class': 'bloc-title'})
            if t_ville_pays is not None:
                ville_pays = t_ville_pays.text.strip()                                
            else:
                ville_pays = "TOGO"

        t_localisation = soup.find('div', {'class': 'bloc-title'})
            if t_localisation is not None:
                localisation = t_localisation.text.strip()                                
            else:
                localisation = None
        
        p = (nom, tel, Qt, ville_pays, localisation)
        l = pharmacies.append(p)
        
        time.sleep(3)

# Part Two : Processing

try:
    dbconnect = sqlite3.connect('db.db')
    print("Connexion à la database effectué")

    dbconnect.executemany("INSERT INTO WaPharmacieGarde (nom,telephone,Quartier,Ville_Pays,Localisation) \
                    VALUES (?,?,?,?,?)", pharmacies);

    dbconnect.commit()       # Commit vers la database
    dbconnect.close()       # Fermeture de la database
except:
    print("Une erreur s'est produite pd de l'ouverture de la database")