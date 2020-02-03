"""
sample_scrapper.py

This updated version scraps from active static
LoL eSports website.
@version: 1.3
@author: Brian Jacobe

"""

import requests
import csv
from bs4 import BeautifulSoup

# Using request module, get function provides
# access to the webpage within the argument.
result = requests.get("https://www.lolesports.com/en_US/teams")

# To make sure that the site is accessible, print
# the result code. 200 OK response code to indicate
# that the page is present.

status = result.status_code
# print(result.status_code)

# Returns the content of the web page
# using HTML parsing library built within
# BeautifulSoup

if status == 200:
    soup = BeautifulSoup(result.content, 'html5lib')
    teams = list()

    # Data is nested with a div whose class
    # is 'team'. Store all information into a dictionary
    # using the find_all function.
    for row in soup.find_all('div', attrs={'class':'team'}):
        team = {}
        team['LCS Team'] = row.h2.text
        team['Description'] = row.h5.text
        teams.append(team)

    # Save all data appended into 'teams' dictionary in a
    # CSV file.
    filename = "lcs_teams_2019.csv"
    with open(filename, 'w') as f:
        w = csv.DictWriter(f,['LCS Team', 'Description'])
        w.writeheader()
        for team in teams:
            w.writerow(team)
else:
    print(f'Error: ' + str(status))

