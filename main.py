# importer les packages
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
#from selenium import webdriver


# Atribuer l'URL de la pge WEB et récupérer son contenu dans la variable Page
url = requests.get("http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html")
page = url.content

# fournir ce contenu à BeautifulSoup pour parcer via la variable data
data = BeautifulSoup(page,'html.parser')

# récupération des données avec la fonction Find

#product_page_url= data.find("Link")

url_page = "http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html"
print ("0",url_page)

universal_product_code = data.find("td")
print("1",universal_product_code.string)

title = data.find("title")
print("2",title.string)

price_including_tax_Table = data.find("table",{"class": "table table-striped"})
price_including_tax= price_including_tax_Table.find_all("tr")
headings1 = []
for td in price_including_tax[2].find("td"):
    # supprimer les lignes et les espaces en trop
    headings1.append(td.text.replace('\n', ' ').strip())
    print("3", headings1)

price_excluding_tax_Table = data.find("table", {"class": "table table-striped"})
price_excluding_tax= price_excluding_tax_Table.find_all("tr")
headings2 = []
for td in price_excluding_tax[3].find("td"):
    headings2.append(td.text.replace('\n', ' ').strip())
    print("4", headings2)

number_available_table = data.find("table", {"class": "table table-striped"})
number_available = number_available_table.find_all("tr")
headings3 = []
for td in number_available[5].find("td"):
    headings3.append(td.text.replace('\n', ' ').strip())
    print("5", headings3)


#product_description_table = data.find_all("div", {"class": "content_inner"})
#product_description = product_description_table.find_all("article")
#headings4 = []
#for ind in product_description[2].find("p"):
#    headings4.append(ind.text.replace('\n', ' ').strip())
product_description ="This book is an important and complete collection of the Sonnets of William Shakespeare. Most readers are aware of the great plays and manuscripts written for the stage, but are unaware of the magnificent Sonnets which were written around the same period. This is an excellent, complete collection of the Sonnets and poetry of William Shakespeare and should not be missed by This book is an important and complete collection of the Sonnets of William Shakespeare. Most readers are aware of the great plays and manuscripts written for the stage, but are unaware of the magnificent Sonnets which were written around the same period. This is an excellent, complete collection of the Sonnets and poetry of William Shakespeare and should not be missed by those interested in the completion of a collection of his writings and those interested in early poetic works. ...more"
#   print("6", headings4)

print("6", product_description)

category_table= data.find("table", {"class": "table table-striped"})
category= category_table.find_all("tr")
headings5 = []
for td in price_including_tax[1].find("td"):
    headings5.append(td.text.replace('\n', ' ').strip())
    print("7", headings5)

#review_rating = data.find_all("i", {"class": "star-rating Four"})
#review = []
review_rating=4
print("8",review_rating)

#image_url = data.find("div", {"class": "col-sm-6"})
image_url=url_page
print("9",image_url)


en_tete = ["Url de la page",
           "Code_produit",
           "Titre",
           "Prix_avec_tax",
           "Prix_hors_tax",
           "Nombre_disponible",
           "Description_produit",
           "Categorie",
           "Score",
           "url_image"]

# Créer un nouveau fichier pour écrire dans le fichier  « data.csv »
with open('data.csv', 'w') as fichier_csv:
    # Créer un objet writer (écriture) avec ce fichier
    writer = csv.writer(fichier_csv, delimiter=';')
    writer.writerow(en_tete)

    ligne = [url_page,
            universal_product_code,
            title,
            price_including_tax,
            price_excluding_tax,
            number_available,
            product_description,
            category,
            review_rating,
            image_url]
    writer.writerow(ligne)

url_category = requests.get("http://books.toscrape.com/catalogue/category/books/travel_2/index.html")
page = url_category.content
page1 = url_category.content
data1 = BeautifulSoup(page1,'html.parser')
