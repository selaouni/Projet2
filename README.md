#  Openclassrooms - parcours "Developpeur d'application python" - Projet2

Date: Avril 2022


Project Title:
Utilisez les bases de Python pour l'analyse de marché

Description:
Scraping du site internet: https://books.toscrape.com/index.html
Le script consulte le site, extrait toutes les catégories de livres disponibles, puis extrait les informations produit de tous les livres appartenant à toutes les différentes catégories, il permet ausso de télecharger er de sauvegarder le fichier image de chaque page Produit consulté.

Getting Started
 
Pour commencer à travailler sur ce projet:

    - créez et activez un environnement virtuel, puis installez les paquets necessaire à l'aide du fichier requirement.txt en utilisant la commande: 
        pip install -r requirements.txt
    - Créer le projet P2_Analyse du marché  dans un dossier 
    - Clonner le repo distant dans votre repo local
    - Executez le script: notez que l'execution de ce script genere 50 fichier csv et 1000 fichier images, le temps d'execution est donc un peu long.
 
 
 libraries utilisé:
    import csv
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    from requests.packages.urllib3.exceptions import InsecureRequestWarning # disable warning
    import os.path
    import urllib.request
    

  Executing program$
  - ce projet a été developpé avec Pycharm
  - -

  Help:
  Any advise for common problems or issues.
  Ajout du code:
              from requests.packages.urllib3.exceptions import InsecureRequestWarning
              requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
  pour desactiver les warning lors du scraping des pages web



  Authors:
  
  Contributors names
    - Sabah ELAOUNI
    - Driss Benjeloun (Mentor)

 Version History:
 
  Sauvegarde des images de la Partie 4 + Ajout du code de la pagination Sabah 00h30 20/04/2022
  Merge remote-tracking branch 'origin/main' Sabah 19/04/2022 18:20
  Partie 3: écriture les données dans un fichier CSV distinct pour chaque catégorie de livres Sabah 18/04/2022 18:17
  Partie 3: Extraction de toutes les catégories de livres avec les données des leurs produits (livres) Sabah 18/04/2022 16:48
  Partie 3: Extraction de toutes les catégories de livres disponibles, Sabah 15/04/2022 19:34
  Partie 2: correction des URL extraits en double Sabah 14/04/2022 17:20
  Partie 2: Extraction des données d'une catégorie sous un seul fichier CSV Sabah 14/04/2022 14:23
  Partie 2: Ajustement du code Sabah 13/04/2022 08:51
  Partie 2: Ajustement des liens en ajoutant le http et  création de la boucle for pour extraction de toutes les donées de la catégorie choisie Sabah 12/04/2022 19:06
  Correction de l'extraction des liens et création du fichier CSV avec l'entete et liens dans la 1ere colonne Sabah 11/04/2022 22:46
  Ajustement de l'affichage du fichier data.csv Sabah 11/04/2022 16:20
  Partie2: extraction des URLs des pages Produit de chaque livre appartenant à une catégorie. Sabah 10/04/2022 19:44
  Partie1: Récupération des données sous fichiers CSV Sabah 09/04/2022 08:51
  Partie1: Correction de la récupération des données Sabah 08/04/2022 15:49
  Charger les données dans le fchier "data.csv" ajutement du code Sabah 06/04/2022 19:29
  Charger les données dans le fchier "data.csv" Sabah 06/04/2022 18:34
  Récupération des donnée de la page HTML Sabah 06/04/2022 17:35


  Acknowledgments:
  
    Inspiration, code snippets, etc.

- https://stackoverflow.com/
- https://www.pluralsight.com/
- https://askcodez.com/
- https://www.browserstack.com
- https://oxylabs.io/blog
- https://www.w3schools.com/
- Groupe Workplaace : [OC] IDF E-learning - Région Ile de France
-
-
-
