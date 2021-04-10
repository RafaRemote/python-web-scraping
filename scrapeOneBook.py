# Purpose of this script:
# 
# First: choose a product page on books.toscrape.com, then:
# 
# replace the url variable defined below by the one of the product page you have chosen
# 
# launch the script: python3 scrapeOneBook.py
# 
# the script will extract the following 10 informations:
# 
# product_page_url
# universal_ product_code (upc)
# title
# price_including_tax
# price_excluding_tax
# number_available
# product_description
# category
# review_rating
# image_url
# 
# Then:
# the script will write a csv file (dataOneBook.csv) with all these datas above.
# dataOneBook.csv will appear in th same folder as scrapeOneBook.py is.

import requests # to make the get request to the url
from bs4 import BeautifulSoup # to parse the html
import csv # to write the csv file
import re # for regex operations

# declaration of variables: url is the url that will be parsed
url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
urlbase = 'https://books.toscrape.com/'
# creating the csv file with the name of the columns
with open("dataOneBook.csv", 'a', newline='') as a_csv_csv:
            csv_writer = csv.writer(a_csv_csv)
            csv_writer.writerow(['product_page_url', 'universal_product_code(upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])

# function to find the review_rating
def find_rating(string_to_parse):
    raitings = {'One': 1, 'Two': 2, 'Three': 3, "Four": 4, "Five": 5}
    review_rating = None
    for rating in ['One', 'Two', 'Three', 'Four', 'Five']:
        if string_to_parse.find(rating) != -1:
            review_rating = raitings[rating]
            return review_rating

# defining the function to find all the datas listed in the intro-description
# using a function, because it will be reused in another module
def find_datas(url_to_parse, a_csv):
    response = requests.get(url_to_parse) # requesting
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml') # to parse the html
        upc = soup.find('td').text # find universal_ product_code
        title = soup.find('h1').text # find title
        price_including_tax = soup.findAll('td')[3].text[1:] # find price incl tax, with the £ sign
        price_excluding_tax = soup.findAll('td')[2].text[1:] # find price excl tax, with the £ sign
        number_available = str(re.findall('[0-9]+', soup.findAll('td')[5].text))[2:4] # find the number_available
        product_description = soup.findAll('p')[3].text # find the description
        category = soup.findAll('a')[3].text  # find the category
        review_rating = find_rating(str(soup.find("p", {"class": "star-rating"})))  # find the review_rating using the function defined above 
        image_url = urlbase + soup.find("img")['src'][5:] # find the image_url
        with open(a_csv, 'a', newline='') as a_csv_csv:
            csv_writer = csv.writer(a_csv_csv)
            csv_writer.writerow([url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url ])
    else:
        print('not able to get this url')

# calling the function
find_datas(url, "dataOneBook.csv")