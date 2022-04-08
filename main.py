# importer les packages
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup


# Atribuer l'URL de la pge WEB et récupérer son contenu dans la variable Page
url = requests.get("http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html")
page = url.content

# fournir ce contenu à BeautifulSoup pour parcer via la variable data
data = BeautifulSoup(page,'html.parser')

# récupération des données avec la fonction Find

#product_page_url= data.find("Link")

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

number_available = data.find("p", {"class": "instock availability"})
price_including_tax= price_including_tax_Table.find_all("tr")
headings3 = []
for td in price_including_tax[5].find("td"):
    headings3.append(td.text.replace('\n', ' ').strip())
    print("5", headings3)


product_description_table = data.find("article", {"class": "product_page"})
product_description = product_description_table.find("p")
headings4 = []
for p in product_description[3].find("p"):
    headings4.append(p.text.replace('\n', ' ').strip())
    print("6", headings4)
#print("6",product_description)

category= data.find("tr", {"class": "table table-striped"})
print("7",category)

review_rating = data.find_all("i", {"class": "icon-star"})
print("8",review_rating)

image_url = data.find("div", {"class": "col-sm-6"})
print("9",image_url)


