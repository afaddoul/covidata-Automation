from datetime import datetime
from pprint import pprint
import json
import sys
sys.path.insert(0, '/Users/q-beast/Desktop/covidata-Automation')
from scraping_scripts import regions_cases_scraper as regions
from scraping_scripts import total_cases_scraper as total

# set json file name
json_file = '../json_output/data_per_day.json'

# read json file
with open(json_file) as f:
    json_days = json.load(f)

regions_cases_dict = regions.regions_cases_scraper()
total_cases_dict = total.total_cases_scraper()

pprint(json_days)
