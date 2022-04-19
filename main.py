# importer les packages
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
#python request remove warning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#pour l'ecriture sur plusieurs fichiers CSV
import glob

###----------------------------------------------------PARTIE2---------------------------------------------------------
"""
url2 = "https://books.toscrape.com/catalogue/category/books/childrens_11/index.html"

while True:

    url_category = requests.get(url2)
    #page1 = url_category.content
    data = BeautifulSoup(url_category.text,'html.parser')

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

    with open('test.csv', 'w') as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=';', lineterminator='\n')
        writer.writerow(en_tete)

    url_list = []
    for lk in data.find_all("li", class_= "col-xs-6 col-sm-4 col-md-3 col-lg-3"):
        for i in lk.find ("div", {"class": "image_container"}).find_all("a"):
            url_list.append(i["href"])

    for url in url_list:
            url = urljoin(url2, url)
        #print("liste urls", url)


            req_data = requests.get(url)
            data1 = BeautifulSoup(req_data.text, "html.parser")


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

            with open('test.csv', 'a', encoding = "utf-8") as csv_file:
                writer = csv.writer(csv_file, delimiter=';', lineterminator='\n')

                for i in ligne_data:
                    writer.writerow(i)

    # Trouver la page suivante à parcer dans la pagination.
    next_page_element = data.select_one('li.next > a')
    if next_page_element:
        next_page_url = next_page_element.get('href')
        url2 = urljoin(url2, next_page_url)
    else:
        break

"""
###----------------------------------------------------PARTIE3---------------------------------------------------------

url_site = "https://books.toscrape.com/index.html"
get_url_page = requests.get(url_site,verify = False)
page_content = get_url_page.content
#récupérataion du contenu de la page
data1 = BeautifulSoup(page_content ,'html.parser')

#récupération de tous les liens de toutes les catégories

category_list=[]

for lk in data1.find_all("ul", class_= "nav nav-list"):
    for i in lk.find ("ul").find_all("a"):
        category_list.append(i["href"])
        category_name = lk.find("a")
        #print(category_name)


for url in category_list:
    category_url = urljoin(url_site, url) #ajout du Https:// pour un lien de site valide
    print("Catégorie", category_url)

    # Ok jusque là-------------------

    req_data = requests.get(category_url) # url categorie récuperé
    my_data = BeautifulSoup(req_data.text, "html.parser")

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

    with open((str(category_name) + ".csv"), 'a', encoding="utf-8") as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=';', lineterminator='\n')
        writer.writerow(en_tete)
    url_list = []
    for lk in my_data.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):
        for i in lk.find("div", {"class": "image_container"}).find_all("a"):
            url_list.append(i["href"])

    for url2 in url_list:
        product_url = urljoin(category_url,url2 )
        print("Produit", product_url)

        req_data2 = requests.get(product_url)  # url produit récuperé
        my_data2 = BeautifulSoup(req_data2.text, "html.parser")

        url_page = product_url
        print("0",url_page)
        # ---------------------------------------
        universal_product_code_data = my_data2.find("td")
        universal_product_code = universal_product_code_data.string
        print("1", universal_product_code)
        # ----------------------------------------
        title_data = my_data2.find("title")
        title = title_data.string
        print("2", title)
        # ---------------------------------------
        price_including_tax_Table = my_data2.find("table", {"class": "table table-striped"})
        price_including_tax_data = price_including_tax_Table.find_all("tr")
        price_including_tax = []
        for td in price_including_tax_data[2].find("td"):
            # supprimer les lignes et les espaces en trop
            price_including_tax.append(td.text.replace('\n', ' ').strip())
            print("3", price_including_tax)
        # --------------------------------
        price_excluding_tax_Table = my_data2.find("table", {"class": "table table-striped"})
        price_excluding_tax_data = price_excluding_tax_Table.find_all("tr")
        price_excluding_tax = []
        for td in price_excluding_tax_data[3].find("td"):
            price_excluding_tax.append(td.text.replace('\n', ' ').strip())
            print("4", price_excluding_tax)
        # ----------------------------------
        number_available_table = my_data2.find("table", {"class": "table table-striped"})
        number_available_data = number_available_table.find_all("tr")
        number_available = []
        for td in number_available_data[5].find("td"):
            number_available.append(td.text.replace('\n', ' ').strip())
            print("5", number_available)

        # ----------------------------------
        product_description = my_data2.find("meta", {"name": "description"})['content']
        print("6", product_description)
        # ----------------------------------
        category_table = my_data2.find("ul", {"class": "breadcrumb"})
        category_data = category_table.find_all("li")
        category = []
        for td in category_data[2].find("a"):
            category.append(td.text.replace('\n', ' ').strip())
            print("7", category)
        # création de l'entete du fichier csv avec le nom de la catégorie en question

        # -----------------------------------
        review_rating_table = my_data2.find("table", {"class": "table table-striped"})
        review_rating_data = review_rating_table("tr")
        review_rating = []
        for td in review_rating_data[6].find("td"):
            review_rating.append(td.text.replace('\n', ' ').strip())
            print("7", review_rating)
        # ----------------------------------
        image = my_data2.find("div", {"class": "item active"})
        for i in image.find_all("img"):
            url_brut = i.get('src')
            image_url = urljoin(product_url, url_brut)
            print("9", image_url)
    # ----------------------------------
    # enregister l'ensemble dans un seul fichier CSV




        with open((str(category_name)+ ".csv"), 'a', encoding = "utf-8") as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=';', lineterminator='\n')


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


            for i in ligne_data:
                writer.writerow(i)


