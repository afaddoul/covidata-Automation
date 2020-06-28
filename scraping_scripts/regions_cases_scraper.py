"""
@author: q-beast
"""

import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint


def regions_cases_scraper():
    # Set target URL
    url = 'https://covid.hespress.com/'

    # Get html Source code
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

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
                "region_name_en": "Béni Mellal-Khénifra",
                "region_code": "MA05",
                "region_name_ar": "بني ملال - خنيفرة",
                "confirmed": lst[6]
            },
            {
                "region_name_en": "Casablanca-Settat",
                "region_code": "MA06",
                "region_name_ar": "الدار البيضاء - سطات",
                "confirmed": lst[0]
            },
            {
                "region_name_en": "Drâa-Tafilalet",
                "region_code": "MA08",
                "region_name_ar": "درعة تافيلالت",
                "confirmed": lst[9]
            },
            {
                "region_name_en": "Dakhla-Oued Ed-Dahab",
                "region_code": "MA12",
                "region_name_ar": "الداخلة - وادي الذهب",
                "confirmed": lst[7]
            },
            {
                "region_name_en": "Fès-Meknès",
                "region_code": "MA03",
                "region_name_ar": "فاس - مكناس",
                "confirmed": lst[3]
            },
            {
                "region_name_en": "Guelmim-Oued Noun",
                "region_code": "MA10",
                "region_name_ar": "كلميم - واد نون",
                "confirmed": lst[8]
            },
            {
                "region_name_en": "Laâyoune-Sakia El Hamra",
                "region_code": "MA11",
                "region_name_ar": "العيون - الساقية الحمراء",
                "confirmed": lst[1]
            },
            {
                "region_name_en": "Marrakech-Safi",
                "region_code": "MA07",
                "region_name_ar": "مراكش - أسفي",
                "confirmed": lst[4]
            },
            {
                "region_name_en": "l'Oriental",
                "region_code": "MA02",
                "region_name_ar": "الجهة الشرقية",
                "confirmed": lst[10]
            },
            {
                "region_name_en": "Rabat-Salé-Kénitra",
                "region_code": "MA04",
                "region_name_ar": "الرباط - سلا - القنيطرة",
                "confirmed": lst[5]
            },
            {
                "region_name_en": "Souss-Massa",
                "region_code": "MA09",
                "region_name_ar": "سوس - ماسة",
                "confirmed": lst[11]
            },
            {
                "region_name_en": "Tanger-Tétouan-Al Hoceïma",
                "region_code": "MA01",
                "region_name_ar": "طنجة - تطوان - الحسيمة",
                "confirmed": lst[2]
            },
        ]
    }
    return (regions_properties)
