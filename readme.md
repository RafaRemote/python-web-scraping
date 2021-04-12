# Project: Price Scraping

Here are the 4 scripts you asked for.

Target Website use for these processes: _books.toscrape.com_


## Instructions

Once you have cloned this repository, in the folder where you have cloned 'python-web-scraping', create the folders: *scraped_datas* and *scraped_images*.

Check the descriptions of the scripts you want to use before using them.

Open a terminal and check that you are in the folder: 'python-web-scraping', then:

you can use the scripts by typing:

'python3 scrapeOneBook.py'

or

'python3 scrapeBooksPerOneCategory.py'

or

'python3 scrapeBooksPerAllCategories.py'

or

'python3 scrapeImageOfEachProductSeen.py'

## Descriptions of scripts

_Note that each scripts will extract informations and that these informations will be stored in the folder: *scraped_datas* for the csv files amd in the folder *scraped_images* for the image files._

### 1. scrapeOneBook.py

will extract the following datas:

* product_page_url
* universal_ product_code (upc)
* title
* price_including_tax
* price_excluding_tax
* number_available
* product_description
* category
* review_rating
* image_url

and will write them in a file: dataOneBook_[name of the book].csv

### 2. scrapeBooksPerCategory.py

will extract the product url of each book for one category, then it will concatenate this information with the 10 other ones listed above.

will write a file: dateBooksPerCategory_[category].csv

### 3. scrapeBooksPerAllCategories.py

will extract all the informations for each book of each categories. 

will write one csv file for each category, using the same form defined above: dateBooksPerCategory_[category].csv

### 4. scrapeImageOfEachProductSeen.py

will save the images of the products that you have visited in the folder *scraped_images*.