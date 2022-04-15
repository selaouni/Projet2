# importer les packages
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urljoin
#python request remove warning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
###----------------------------------------------------PARTIE1---------------------------------------------------------
"""
# Atribuer l'URL de la pge WEB et récupérer son contenu dans la variable Page

url = requests.get("http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html")
page = url.content

# fournir ce contenu à BeautifulSoup pour parcer via la variable data
data = BeautifulSoup(page, 'html.parser')


# récupération du lien de la page

# driver = webdriver.Chrome()
# ouvrir l'URL
# driver.get("http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html")
# url_page = driver.current_url
url_page="http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html"
print("0", url_page)

# récupération des données avec la fonction Find
#---------------------------------------
universal_product_code_data = data.find("td")
universal_product_code = universal_product_code_data.string
print("1",universal_product_code.string)
#----------------------------------------
title_data = data.find("title")
title = title_data.string
print("2",title)
#---------------------------------------
price_including_tax_Table = data.find("table",{"class": "table table-striped"})
price_including_tax_data = price_including_tax_Table.find_all("tr")
price_including_tax = []
for td in price_including_tax_data[2].find("td"):
    # supprimer les lignes et les espaces en trop
    price_including_tax.append(td.text.replace('\n', ' ').strip())
    print("3", price_including_tax)
#--------------------------------
price_excluding_tax_Table = data.find("table", {"class": "table table-striped"})
price_excluding_tax_data= price_excluding_tax_Table.find_all("tr")
price_excluding_tax = []
for td in price_excluding_tax_data[3].find("td"):
    price_excluding_tax.append(td.text.replace('\n', ' ').strip())
    print("4", price_excluding_tax)
#----------------------------------
number_available_table = data.find("table", {"class": "table table-striped"})
number_available_data = number_available_table.find_all("tr")
number_available = []
for td in number_available_data[5].find("td"):
    number_available.append(td.text.replace('\n', ' ').strip())
    print("5", number_available)

#----------------------------------

product_description = data.find("meta", {"name":"description"})['content']
print("6", product_description)

#----------------------------------
category_table= data.find("table", {"class": "table table-striped"})
category_data = category_table.find_all("tr")
category = []
for td in category_data[1].find("td"):
    category.append(td.text.replace('\n', ' ').strip())
    print("7", category)
#-----------------------------------
review_rating_table= data.find("table", {"class": "table table-striped"})
review_rating_data = category_table.find_all("tr")
review_rating = []
for td in review_rating_data[6].find("td"):
    review_rating.append(td.text.replace('\n', ' ').strip())
    print("7", review_rating)
#----------------------------------
#image_url = data.find("div", {"class": "col-sm-6"})
image = data.find("div", {"class": "item active"})
for i in image.find_all("img"):
    image_url = i.get('src')
print("9", image_url)
#----------------------------------

#créer un tableau avec l'entete du ficher csv
en_tete = ["url_page",
           "universal_product_code",
           "title",
           "price_including_tax",
           "price_excluding_tax",
           "number_available",
           "Dproduct_description",
           "category",
           "review_rating",
           "image_url"]

# Créer un nouveau fichier pour écrire dans le fichier  « data.csv »
#f = open("test1.csv", "w")
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
"""
###----------------------------------------------------PARTIE2---------------------------------------------------------

url2 = "https://books.toscrape.com/catalogue/category/books/childrens_11/index.html"
url_category = requests.get(url2,verify=False)
#page1 = url_category.content
data1 = BeautifulSoup(url_category.text,'html.parser')

en_tete = ["url_page",
        "universal_product_code",
        "title",
        "price_including_tax",
        "price_excluding_tax",
        "number_available",
        "Dproduct_description",
        "category",
        "review_rating",
        "image_url"]

with open('data.csv', 'w') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=';', lineterminator='\n')
    writer.writerow(en_tete)


# premiere solution    page_link_global_class = data1.find("ol", {"class": "row"})
    #page_link_class = page_link_global_class.find_all("div",{"class": "image_container"})
    #for lk in page_link_global_class.find_all("a"):
    #    f.write(lk.get('href'))
    #    f.write("\n")
    #    print("partie2", lk.get('href'))


url_list = []

for lk in data1.find_all("li", class_= "col-xs-6 col-sm-4 col-md-3 col-lg-3"):
    for i in lk.find ("div", {"class": "image_container"}).find_all("a"):
        url_list.append(i["href"])

for url in url_list:
        url = urljoin(url2, url)
        #print("liste urls", url)

        req_data = requests.get(url)
        data1 = BeautifulSoup(req_data.text, "html.parser")
    # ---------------------------------------
    #    driver = webdriver.Chrome(ChromeDriverManager().install())
    #    ouvrir l'URL
    #    driver.get("http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html")
    #    url_page = driver.current_url


        url_page = url
        #print("0",url_page)
    # ---------------------------------------
        universal_product_code_data = data1.find("td")
        universal_product_code = universal_product_code_data.string
        #print("1", universal_product_code)
    # ----------------------------------------
        title_data = data1.find("title")
        title = title_data.string
        #print("2", title)
    # ---------------------------------------
        price_including_tax_Table = data1.find("table", {"class": "table table-striped"})
        price_including_tax_data = price_including_tax_Table.find_all("tr")
        price_including_tax = []
        for td in price_including_tax_data[2].find("td"):
        # supprimer les lignes et les espaces en trop
            price_including_tax.append(td.text.replace('\n', ' ').strip())
            #print("3", price_including_tax)
    # --------------------------------
        price_excluding_tax_Table = data1.find("table", {"class": "table table-striped"})
        price_excluding_tax_data = price_excluding_tax_Table.find_all("tr")
        price_excluding_tax = []
        for td in price_excluding_tax_data[3].find("td"):
            price_excluding_tax.append(td.text.replace('\n', ' ').strip())
            #print("4", price_excluding_tax)
    # ----------------------------------
        number_available_table = data1.find("table", {"class": "table table-striped"})
        number_available_data = number_available_table.find_all("tr")
        number_available = []
        for td in number_available_data[5].find("td"):
            number_available.append(td.text.replace('\n', ' ').strip())
            #print("5", number_available)

    # ----------------------------------
        product_description = data1.find("meta", {"name": "description"})['content']
        #print("6", product_description)
    # ----------------------------------
        category_table = data1.find("ul", {"class": "breadcrumb"})
        category_data = category_table.find_all("li")
        category = []
        for td in category_data[2].find("a"):
            category.append(td.text.replace('\n', ' ').strip())
            #print("7", category)
    # -----------------------------------
        review_rating_table = data1.find("table", {"class": "table table-striped"})
        review_rating_data = review_rating_table("tr")
        review_rating = []
        for td in review_rating_data[6].find("td"):
            review_rating.append(td.text.replace('\n', ' ').strip())
            #print("7", review_rating)
    # ----------------------------------
        image = data1.find("div", {"class": "item active"})
        for i in image.find_all("img"):
            url_brut = i.get('src')
            image_url = urljoin(url, url_brut)
            #print("9", image_url)
    # ----------------------------------

# enregister l'ensemble dans un seul fichier CSV

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
        ligne_data = []
        ligne_data.append(ligne)

        with open('data.csv', 'a', encoding="utf-8") as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=';', lineterminator='\n')

            for i in ligne_data:
                writer.writerow(i)



###----------------------------------------------------PARTIE3---------------------------------------------------------

url_page = "https://books.toscrape.com/index.html"
get_url_page = requests.get(url_page,verify = False)
page_content = get_url_page.content
data1 = BeautifulSoup(page_content ,'html.parser')

category_url_list=[]


for lk in data1.find_all("ul", class_= "nav nav-list"):
    for i in lk.find ("ul").find_all("a"):
        category_url_list.append(i["href"])
    print(category_url_list)


"""
for i in lk.find("li").find("a"):

category_table = data1.find("ul", {"class": "nav nav-list"})
category_data = category_table.find_all("li")
category = []
for td in category_data[2].find("a"):
        category.append(td.text.replace('\n', ' ').strip())
        #print("7", category)"""