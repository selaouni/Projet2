# importer les packages
# import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# Atribuer l'URL de la pge WEB et récupérer son contenu dans la variable Page

url = requests.get("http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html")
page = url.content

# fournir ce contenu à BeautifulSoup pour parcer via la variable data
data = BeautifulSoup(page, 'html.parser')


# récupération du lien de la page

#driver = webdriver.Chrome()
# ouvrir l'URL
#driver.get("http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html")
#url_page = driver.current_url
url_page="http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html"
print("0", url_page)

# récupération des données avec la fonction Find

universal_product_code_data = data.find("td")
universal_product_code = universal_product_code_data.string
print("1",universal_product_code.string)

title_data = data.find("title")
title = title_data.string
print("2",title)

price_including_tax_Table = data.find("table",{"class": "table table-striped"})
price_including_tax_data = price_including_tax_Table.find_all("tr")
price_including_tax = []
for td in price_including_tax_data[2].find("td"):
    # supprimer les lignes et les espaces en trop
    price_including_tax.append(td.text.replace('\n', ' ').strip())
    print("3", price_including_tax)

price_excluding_tax_Table = data.find("table", {"class": "table table-striped"})
price_excluding_tax_data= price_excluding_tax_Table.find_all("tr")
price_excluding_tax = []
for td in price_excluding_tax_data[3].find("td"):
    price_excluding_tax.append(td.text.replace('\n', ' ').strip())
    print("4", price_excluding_tax)

number_available_table = data.find("table", {"class": "table table-striped"})
number_available_data = number_available_table.find_all("tr")
number_available = []
for td in number_available_data[5].find("td"):
    number_available.append(td.text.replace('\n', ' ').strip())
    print("5", number_available)


#product_description_table = data.find_all("div", {"class": "content_inner"})
#product_description = product_description_table.find_all("article")
#headings4 = []
#for ind in product_description[2].find("p"):
#    headings4.append(ind.text.replace('\n', ' ').strip())
product_description ="This book is an important and complete collection of the Sonnets of William Shakespeare. Most readers are aware of the great plays and manuscripts written for the stage, but are unaware of the magnificent Sonnets which were written around the same period. This is an excellent, complete collection of the Sonnets and poetry of William Shakespeare and should not be missed by This book is an important and complete collection of the Sonnets of William Shakespeare. Most readers are aware of the great plays and manuscripts written for the stage, but are unaware of the magnificent Sonnets which were written around the same period. This is an excellent, complete collection of the Sonnets and poetry of William Shakespeare and should not be missed by those interested in the completion of a collection of his writings and those interested in early poetic works. ...more"
#   print("6", headings4)

print("6", product_description)

category_table= data.find("table", {"class": "table table-striped"})
category_data = category_table.find_all("tr")
category = []
for td in category_data[1].find("td"):
    category.append(td.text.replace('\n', ' ').strip())
    print("7", category)

review_rating_table= data.find("table", {"class": "table table-striped"})
review_rating_data = category_table.find_all("tr")
review_rating = []
for td in review_rating_data[6].find("td"):
    review_rating.append(td.text.replace('\n', ' ').strip())
    print("7", review_rating)




#image_url = data.find("div", {"class": "col-sm-6"})
image = data.find("div", {"class": "item active"})
for i in image.find_all("img"):
    image_url = i.get('src')
print("9", image_url)


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

###partie 2

url2 = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
url_category = requests.get(url2)
page1 = url_category.content
data1 = BeautifulSoup(page1,'html.parser')

#urls = []
# #for link in data1.find_all('a'):
# #    print(link.get('href'))

# ouvrir un fichier en mode lecture
#f = open("test1.csv", "w")
#for link in data1.find_all("a"):
#    f.write(link.get('href'))
#    f.write("\n")
#f.close()



#f = open("test1.csv", "w")
#page_link_class = data1.find("div",{"class" : "col-sm-8 col-md-9"})
#for link in page_link_class.find_all("div",{"class" : "image_container"}):
#    f.write(link.get('href'))
#   f.write("\n")
#f.close()