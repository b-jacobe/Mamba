"""
scraper.py

version: 1.2
author: Brian Jacobe
"""

import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.passiton.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())
quotes = list()
table = soup.find('div', attrs={'class':'container'})

for row in table.findAll('div', attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {} 
    quote['url'] = row.a['href'] 
    quote['line'] = row.img['alt']
    quote['source'] = row.img['src']
    quotes.append(quote) 

filename = 'inspirational_quotes.csv'

with open(filename, 'w') as f: 
    w = csv.DictWriter(f,['url','line','source']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote) 
