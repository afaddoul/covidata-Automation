"""
@author: q-beast
"""

import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

def total_cases_scraper():
    # Set target URL
    url = 'https://covid.hespress.com/'

    # Get html Source code
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    #*******************************TOTAL PROPERTIES**********************************#
    # Get total properties rows
    rows = soup.findAll('h4', attrs={'class': 'mb-0 font-30'})

    # Parse total properties rows
    lst = []
    for row in rows:
        row = row.text.replace("<h4 class=\"mb-0 font-30\">", "")
        row = row.replace("</h4>", "")
        if (row.isnumeric()):
            lst.append(int(row))
        else:
            lst.append(0)

    # Get total Update date
    rows = soup.findAll('span', attrs={'class': 'font-13'})
    row = rows[0].text.split()

    # Create total properties dictionnary
    total_properties = {
        "date": {
            "update_day": row[3],
            "update_hour": row[6]
        },
        "data": {
            "total_confirmed": lst[0],
            "total_excluded": lst[1],
            "total_recovered": lst[2],
            "total_deaths": lst[3],
            "total_under_treatment": lst[4]
        }
    }
    return total_properties

