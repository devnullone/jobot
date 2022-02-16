ToDo :
- Introduction
- Fonctionalités
- Techno
- BM

### Introduction

Cet projet vise a scrapper des offres d'emploi sur le net et à faire acceder ses informations aux utilisateurs/chommeur(e)s/Diplomé(e)s/etc... au travers d'une interface utilisateur simple et accessible (un botnet whatsapp/telegram , d'un channel telegram ou d'un autre site web).

### Fonctionalités

L'utilisateur pourra: 
- Remplir un formulaire d'information
- Recevoir les offres en fonction des infos recolter via le formulaire d'information
- Choisir de recevoir tel ou tel offres classer selon des domaines d'activités (ie: Agronomie, BTP, Comptabilité etc...) ou par lieu géographique ou encore par mode de travail (présentiels ou en télé-travail)
- Rechercher via des keywords les offres disponibles.
- Postuler aux offres d'emploi
- Ajouter un fichier Cv (Sera envoyer à l'employeur lorsqu'un utilisateur postule à une offre d'emploi)
- Payer pour activer certainses fonctionalités

### Techno

- Beatifull Soup - For Scraping
- Cron Tasks - For automate scraping scripts
- Whatsapp/Telegram Api - For bot creation
- Sqlite3 - For database
- Django/CodeIgniter4 - For small  site web
- Cinetpay Api - For Mobile Payements

----------------------------------------------

Mobile Payements workflow trought chatbot

1- Generate Payement links
2- User follows link to complete payement
  -- User complete sucessfully transaction [Goto 3]
  -- User abort transaction [Goto 1]
3- User recieve activation link/code.
