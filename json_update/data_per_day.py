from datetime import datetime
from pprint import pprint
import json
import sys
sys.path.insert(0, '/Users/q-beast/Desktop/covidata-Automation')
from scraping_scripts import total_cases_scraper as total
from scraping_scripts import daily_cases_scraper as daily

# Set json file name
json_file = '../json_output/data_per_day.json'

# Read json file
with open(json_file) as f:
    json_days = json.load(f)

# Get daily data dict
daily_cases_dict = daily.daily_cases_scraper()

# Set pub date
pub_date = daily_cases_dict['date']['update_day'] + '/' + \
    str(datetime.today().month) + '/' + str(datetime.today().year)[2:]

# Create new element
last_updated_elm = {'deaths': daily_cases_dict['data']['daily_deaths'],
                    'pub_date': pub_date, 'recovered': daily_cases_dict['data']['daily_recovered']}

# Push new element
json_days['data'].append(last_updated_elm)

# Create updated json
f = open("output.json", "w")
json.dump(json_days, f, indent=4,
                           sort_keys=True, ensure_ascii=False)
f.close()
