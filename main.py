# importer les packages
import pandas as pd
import csv
import os
import requests
from bs4 import BeautifulSoup
# Atribuer l'URL de la pge WEB et récupérer son contenu dans la variable Page
url = requests.get("http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html")
page = url.content

# fournir ce contenu à BeautifulSoup pour parcer via la variable data
data = BeautifulSoup(page,'html.parser')

# récupération des données avec la fonction Find

# product_page_url= data.find("h1", {"class": "ico-after ico-tutorials"})

universal_product_code = data.find("td")
print("1",universal_product_code.string)

title = data.find("title")
print("2",title.string)

price_including_tax =data.find("table",{"class": "table table-striped"})
print("3",price_including_tax)

price_excluding_tax = data.find("th", {"class": "table table-striped"})
print("4", price_excluding_tax)

number_available = data.find("p", {"class": "instock availability"})
print("5",number_available)

#product_description = data.find("meta", {"class": "content"})
#print("6",product_description)

category= data.find("tr", {"class": "table table-striped"})
print("7",category)

review_rating = data.find_all("i", {"class": "icon-star"})
print("8",review_rating)

image_url = data.find("div", {"class": "col-sm-6"})
print("9",image_url)

