"""
@author: q-beast
"""

import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint


def daily_cases_scraper():
    # Set target URL
    url = 'https://covid.hespress.com/'

    # Get html Source code
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    rows = soup.findAll('span')
    rows = [rows[2], rows[5], rows[8], rows[11], rows[14]]
    lst = []
    for row in rows:
        row = row.text.replace("i>", "").split()[0]
        if (row.isnumeric()):
            lst.append(int(row))
        else:
            lst.append(0)
    # Get total Update date
    rows = soup.findAll('span', attrs={'class': 'font-13'})
    row = rows[0].text.split()

    # Create daily properties dictionnary
    daily_properties = {
        "date": {
            "update_day": row[3],
            "update_hour": row[6]
        },
        "data": {
            "daily_confirmed": lst[0],
            "daily_excluded": lst[1],
            "daily_recovered": lst[2],
            "daily_deaths": lst[3],
            "daily_under_treatment": lst[4]
        }
    }
    return daily_properties
