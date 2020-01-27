"""
scraper.py

Scraper project that focuses on extracting
Tweets from Bleacher Report's webpage.

version: 1.0
author: Brian Jacobe
"""

import csv
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = "http://www.bloomberg.com/quote/SPX:IND"

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the website into BeautifulSoup and store into variable 'soup'
soup = BeautifulSoup(page, ‘html.parser’)

# Derive <div> of name and retrieve value
name_box = soup.find(‘h1’, attrs={‘class’: ‘name’})

# remove starting and trailing
name = name_box.text.strip()
print(name)

# get the index price
price_box = soup.find(‘div’, attrs={‘class’:’price’})
price = price_box.text
print(price)

# open a csv file with append
with open('index.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])