from datetime import datetime
from pprint import pprint
import json
import sys
sys.path.insert(0, '/Users/q-beast/Desktop/covidata-Automation')
from scraping_scripts import total_cases_scraper as total
from scraping_scripts import daily_cases_scraper as daily


# Set json file name
json_file = '../json_output/data_by_day.json'

# Read json file
with open(json_file) as f:
    json_days = json.load(f)

daily_cases_dict = daily.daily_cases_scraper()
total_cases_dict = total.total_cases_scraper()

#pprint(json_days['data']['Total'])
#print(daily_cases_dict)
#pprint(total_cases_dict)
json_days['data']['Total'][0]['confirmed'] = total_cases_dict['data']['total_confirmed']
json_days['data']['Total'][0]['excluded'] = total_cases_dict['data']['total_excluded']

# Set pub date
pub_date = daily_cases_dict['date']['update_day'] + '/' + \
    str(datetime.today().month) + '/' + str(datetime.today().year)

# Calculate total tested
total = daily_cases_dict['data']['daily_confirmed'] + daily_cases_dict['data']['daily_excluded']

# Create new element
last_updated_elm = {'confirmed': daily_cases_dict['data']['daily_confirmed'],
                    'date': pub_date, 'excluded': daily_cases_dict['data']['daily_excluded'],
                    'total': total
                    }
# Push new element
json_days['data']['Tested'].append(last_updated_elm)

# Create updated json
f = open("output.json", "w")
json.dump(json_days, f, indent=4,
                           sort_keys=True, ensure_ascii=False)
f.close()
