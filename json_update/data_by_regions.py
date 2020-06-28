from scraping_scripts import total_cases_scraper as total
from scraping_scripts import regions_cases_scraper as regions
from datetime import datetime
from pprint import pprint
import json
import sys
sys.path.insert(0, '/Users/q-beast/Desktop/covidata-Automation')

# set json file name
json_file = '../json_output/data_by_regions.json'

# read json file
with open(json_file) as f:
    json_regions = json.load(f)

# Get dicts
regions_cases_dict = regions.regions_cases_scraper()
total_cases_dict = total.total_cases_scraper()

# Update total country cases
json_regions['data']['country'][0]['confirmed'] = total_cases_dict['data']['total_confirmed']
json_regions['data']['country'][0]['deaths'] = total_cases_dict['data']['total_deaths']
json_regions['data']['country'][0]['excluded'] = total_cases_dict['data']['total_excluded']
json_regions['data']['country'][0]['recovered'] = total_cases_dict['data']['total_recovered']

# Update total regions cases
json_regions['data']['regions'][0]['confirmed'] = regions_cases_dict['data'][0]['confirmed']
json_regions['data']['regions'][1]['confirmed'] = regions_cases_dict['data'][1]['confirmed']
json_regions['data']['regions'][2]['confirmed'] = regions_cases_dict['data'][2]['confirmed']
json_regions['data']['regions'][3]['confirmed'] = regions_cases_dict['data'][3]['confirmed']
json_regions['data']['regions'][4]['confirmed'] = regions_cases_dict['data'][4]['confirmed']
json_regions['data']['regions'][5]['confirmed'] = regions_cases_dict['data'][5]['confirmed']
json_regions['data']['regions'][6]['confirmed'] = regions_cases_dict['data'][6]['confirmed']
json_regions['data']['regions'][7]['confirmed'] = regions_cases_dict['data'][7]['confirmed']
json_regions['data']['regions'][8]['confirmed'] = regions_cases_dict['data'][8]['confirmed']
json_regions['data']['regions'][9]['confirmed'] = regions_cases_dict['data'][9]['confirmed']
json_regions['data']['regions'][10]['confirmed'] = regions_cases_dict['data'][10]['confirmed']
json_regions['data']['regions'][11]['confirmed'] = regions_cases_dict['data'][11]['confirmed']

# Update updating time
update_date = str(regions_cases_dict['date']['update_hour']) + ' ' + str(regions_cases_dict['date']
                                                                         ['update_day']) + '-' + str(datetime.today().month) + '-' + str(datetime.today().year)
json_regions['last_updated'] = update_date

# Create updated json file
f = open("output.json", "w")
json.dump(json_regions, f, indent=4, sort_keys=True, ensure_ascii=False)
f.close()
