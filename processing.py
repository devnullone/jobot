import requests
from bs4 import BeautifulSoup
import sqlite3
import time
from datetime import date

emplois =[]
today = date.today()
#Database setup

try:
    dbconnect = sqlite3.connect('db.db')
    print("Connexion à la database effectué")
except:
    print("Une erreur s'est produite pd de l'ouverture de la database")

with open('WaJobsLinks.txt', 'r') as file:
    for line in file:
        #line = 'https://www.emploi.tg/offre-emploi-togo/chef-projet-ran-166603'
        url = line.strip()
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')

            t_titre = soup.find('div', {'class': 'bloc-title'})
            titre = t_titre.text.strip()                                        # Titre de l'annonce

            t_postDate = soup.find('div', {'class': 'job-ad-publication-date'})
            if t_postDate is not None:
                postDate = t_postDate.text.strip()                                  # Date de publication
            else:
                postDate = "Publiée le " + str(today.strftime("%d/%m/%Y"))          # Date actuelle

            t_annonceur = soup.find('div', {'class': 'company-title'})
            if t_annonceur is not None:
                annonceur = t_annonceur.text.strip()                                # Nom de l'Annoceur
            else:
                annonceur = "Aucun"
            t_siteWebDeLannonceur = soup.find('td', {'class': 'website-url'})
            if t_siteWebDeLannonceur is not None:
                siteWebDeLannonceur = t_siteWebDeLannonceur.text.strip()            # Site Web de l'Annoceur
            else:
                siteWebDeLannonceur = "N/A"                                            # Aucun site web

            t_sectorDeLannonceur = soup.find('td', {'class': 'sector-title'})
            if t_sectorDeLannonceur is not None:
                sectorDeLannonceur = t_sectorDeLannonceur.text.strip()              # Secteur d'activité de l'Annoceur
            else:
                sectorDeLannonceur = "Aucun"                                             #Aucun secteur d'activité

            t_annonce = soup.select('div[id*="job-ad-details-"]')
            if t_annonce is not None:
                annonce = t_annonce[0].text.strip()                                 # Offre proprement dite.
            else:
                annonce = "N/A"                                                     # Pas de description

            t = (titre, postDate, annonceur, siteWebDeLannonceur, sectorDeLannonceur, annonce)
            l = emplois.append(t)
            #print(len(emplois),'entrés')
            time.sleep(3)

#print('Je suis sortie de la boucle', len(emplois),' entrer')

# Insertion Multiple dans la database
# dbconnect.executemany('INSERT INTO q1_person_name(first_name, last_name) VALUES (?,?)', data_person_name)

dbconnect.executemany("INSERT INTO WaEmplois (title,postDate,annoceur,annonceurWeb,annonceurSecteurDactivite,annonceBody) \
                    VALUES (?,?,?,?,?,?)", emplois);

dbconnect.commit()       # Commit vers la database
dbconnect.close()       # Fermeture de la database

# Insertion Unique dans la database
#cur.execute("insert into contacts (name, phone, email) values (?, ?, ?)",
#            (name, phone, email))

print("End")