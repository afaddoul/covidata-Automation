"""
@author: q-beast
"""

import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

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
#*******************************DAILY PROPERTIES*********************************#
# Parse daily properties rows
rows = soup.findAll('span')
rows = [rows[2], rows[5], rows[8], rows[11], rows[14]]
lst = []
for row in rows:
    row = row.text.replace("i>", "").split()[0]
    if (row.isnumeric()):
        lst.append(int(row[0]))
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

#*******************************REGIONS PROPERTIES*******************************#
# Get regions cases rows
rows = soup.findAll('td')

# Parse total regions cases
lst = []
i = 0
for row in rows:
    i += 1
    if (i % 2) != 0:
        lst.append(int(row.text))

# Get regions update date
rows = soup.findAll(
    'h6', attrs={'class': 'card-subtitle mt-1 text-muted mb-0'})
row = rows[0].text.split()

# Create regions properties dictionnary
regions_properties = {
    "date": {
        "update_day": row[3],
        "update_hour": row[6]
    },
    "data": [
        {
            "region_name_en": "Casablanca-Settat",
            "region_code": "MA06",
            "region_name_ar": "الدار البيضاء - سطات",
            "confirmed": lst[0]
        },
        {
            "region_name_en": "Laâyoune-Sakia El Hamra",
            "region_code": "MA11",
            "region_name_ar": "العيون - الساقية الحمراء",
            "confirmed": lst[1]
        },
        {
            "region_name_en": "Tanger-Tétouan-Al Hoceïma",
            "region_code": "MA01",
            "region_name_ar": "طنجة - تطوان - الحسيمة",
            "confirmed": lst[2]
        },
        {
            "region_name_en": "Fès-Meknès",
            "region_code": "MA03",
            "region_name_ar": "فاس - مكناس",
            "confirmed": lst[3]
        },
        {
            "region_name_en": "Marrakech-Safi",
            "region_code": "MA07",
            "region_name_ar": "مراكش - أسفي",
            "confirmed": lst[4]
        },
        {
            "region_name_en": "Rabat-Salé-Kénitra",
            "region_code": "MA04",
            "region_name_ar": "الرباط - سلا - القنيطرة",
            "confirmed": lst[5]
        },
        {
            "region_name_en": "Béni Mellal-Khénifra",
            "region_code": "MA05",
            "region_name_ar": "بني ملال - خنيفرة",
            "confirmed": lst[6]
        },
        {
            "region_name_en": "Dakhla-Oued Ed-Dahab",
            "region_code": "MA12",
            "region_name_ar": "الداخلة - وادي الذهب",
            "confirmed": lst[7]
        },
        {
            "region_name_en": "Guelmim-Oued Noun",
            "region_code": "MA10",
            "region_name_ar": "كلميم - واد نون",
            "confirmed": lst[8]
        },
        {
            "region_name_en": "Drâa-Tafilalet",
            "region_code": "MA08",
            "region_name_ar": "درعة تافيلالت",
            "confirmed": lst[9]
        },
        {
            "region_name_en": "l'Oriental",
            "region_code": "MA02",
            "region_name_ar": "الجهة الشرقية",
            "confirmed": lst[10]
        },

        {
            "region_name_en": "Souss-Massa",
            "region_code": "MA09",
            "region_name_ar": "سوس - ماسة",
            "confirmed": lst[11]
        },
    ]
}

pprint(total_properties)
print("\n")
pprint(daily_properties)
print("\n")
pprint(regions_properties)
