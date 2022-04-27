# Openclassrooms / Projet2 - parcours "Developpeur d'application python"

* Date: Avril 2022 *


## Titre du projet:  
Utilisez les bases de Python pour l'analyse de marché

## Description:   
Scraping du site internet: https://books.toscrape.com/index.html.    
Le script consulte le site, extrait toutes les catégories de livres disponibles, puis extrait les informations produit de tous les livres appartenant à toutes les   différentes catégories.   
Ci dessous les informations extraites par produit:
- product_page_url  
- universal_ product_code (upc)  
- title  
- price_including_tax  
- price_excluding_tax  
- number_available  
- product_description  
- category  
- review_rating  
- image_url  

Toutes ces informations sont sauvregardées dans des fichiers CSV (un CSV par catégorie).    
ce programme permet aussi de télecharger et de sauvegarder le fichier image de chaque page produit consultée.  

## Exécution du programme  
*Ce projet a été developpé avec Pycharm*  
Pour commencer à travailler sur ce projet:  

    - Créez et activez l'environnement virtuel, puis installez les paquets necessaires à l'aide du fichier requirement.txt en utilisant la commande:   
        pip install -r requirements.txt  
    - Créer le projet P2_Analyse du marché  dans un dossier   
    - Clonner le repo distant dans votre repo local  
    - Executez le script: notez que l'execution de ce script génére 50 fichiers csv et 1000 fichiers image, le temps d'execution est donc un peu long.  
 
 
 ## libraries utilisées:  
 `import csv`    
 `import requests`    
 `from bs4 import BeautifulSoup`    
 `from urllib.parse import urljoin`    
 `from requests.packages.urllib3.exceptions import InsecureRequestWarning # disable warning`    
 `import os.path`  
 `import urllib.request`  
 `import re` 
   
  ## Aide:  
  *Any advise for common problems or issue*  
  le code suivant a été ajouté dans le script pour desactiver les warning lors du scraping des pages web:  
              `from requests.packages.urllib3.exceptions import InsecureRequestWarning`  
              `requests.packages.urllib3.disable_warnings(InsecureRequestWarning)`  
  
  ## Contributeurs:    
    - Sabah ELAOUNI    
    - Driss Benjeloun (Mentor)  

 ## Historique des Versions:    
 *principales versions sous Github*
  - Vérification globale et génération de la version finale du projet Sabah 27/04/2022 19:59  
  - Sauvegarde des images et Ajout du code de la pagination Sabah 00h30 20/04/2022  
  - Ecriture les données dans un fichier CSV distinct pour chaque catégorie de livres Sabah 18/04/2022 18:17  
  - Extraction de toutes les catégories de livres avec les données de leurs produits (livres) Sabah 18/04/2022 16:48  
  - Extraction de toutes les catégories de livres disponibles, Sabah 15/04/2022 19:34  
  - Extraction des données d'une catégorie sous un seul fichier CSV Sabah 14/04/2022 14:23  
  - Extraction des URLs des pages Produit de chaque livre appartenant à une catégorie. Sabah 10/04/2022 19:44  
  - Récupération des données sous fichiers CSV Sabah 09/04/2022 08:51  
  - Récupération des donnée de la page HTML Sabah 06/04/2022 17:35  


  ## Acknowledgments: (Inspiration, code snippets ...)  

- https://stackoverflow.com/    
- https://www.pluralsight.com/    
- https://askcodez.com/    
- https://www.browserstack.com    
- https://oxylabs.io/blog    
- https://www.w3schools.com/    
- https://www.developpez.net/forums
- Groupe Workplaace : [OC] IDF E-learning - Région Ile de France    



