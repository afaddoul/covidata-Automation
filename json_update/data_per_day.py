from datetime import datetime
from pprint import pprint
import json
import sys
sys.path.insert(0, '/Users/q-beast/Desktop/covidata-Automation')
from scraping_scripts import daily_cases_scraper as daily
from scraping_scripts import total_cases_scraper as total

# set json file name
json_file = '../json_output/data_per_day.json'

# read json file
with open(json_file) as f:
    json_days = json.load(f)

daily_cases_dict = daily.daily_cases_scraper()

pub_date = daily_cases_dict['date']['update_day'] + '/' + str(datetime.today().month) + '/' + str(datetime.today().year)[2:]

last_updated_elm = {'deaths': daily_cases_dict['data']['daily_deaths'], 'pub_date': pub_date, 'recovered': daily_cases_dict['data']['daily_recovered']}
json_days['data'].append(last_updated_elm)

f = open("output.json", "w")
json_countries = json.dump(json_days, f, indent=4, sort_keys=True, ensure_ascii=False)
f.close()
