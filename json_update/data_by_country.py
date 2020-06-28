import csv, json
import os
from pprint import pprint
from operator import itemgetter

#set json file name
json_file = '../json_output/data_by_country.json'

# set CSSE dir path
csse_dir = '/Users/q-beast/Desktop/covidata-Automation/COVID-19/csse_covid_19_data/csse_covid_19_time_series/'

#set file path
confirmed_file = csse_dir + 'time_series_covid19_confirmed_global.csv'
deaths_file = csse_dir + 'time_series_covid19_deaths_global.csv'
recovered_file = csse_dir + 'time_series_covid19_recovered_global.csv'

#init data lists
confirmed_data = []
deaths_data = []
recovered_data = []

#read csv files
with open(confirmed_file) as f:
	for row in csv.DictReader(f):
		confirmed_data.append(row)

with open(deaths_file) as f:
	for row in csv.DictReader(f):
		deaths_data.append(row)

with open(recovered_file) as f:
	for row in csv.DictReader(f):
		recovered_data.append(row)

#read json file
with open(json_file) as f:
  json_countries = json.load(f)

#**************************CONFIRMED CASES PARSING*****************************#

#Get confirmed data for each country
confirmed_data_algeria = json.dumps(confirmed_data[2])
confirmed_data_tunisia = json.dumps(confirmed_data[212])
confirmed_data_egypt = json.dumps(confirmed_data[98])
confirmed_data_mauritania = json.dumps(confirmed_data[156])
confirmed_data_libya = json.dumps(confirmed_data[239])

#load confirmed data for each country
confirmed_data_algeria = json.loads(confirmed_data_algeria)
confirmed_data_tunisia = json.loads(confirmed_data_tunisia)
confirmed_data_egypt = json.loads(confirmed_data_egypt)
confirmed_data_mauritania = json.loads(confirmed_data_mauritania)
confirmed_data_libya = json.loads(confirmed_data_libya)

#get list of keys for confirmed data
algeria_lst = list(map(itemgetter(0), confirmed_data_algeria.items()))
tunisia_lst = list(map(itemgetter(0), confirmed_data_tunisia.items()))
egypt_lst = list(map(itemgetter(0), confirmed_data_egypt.items()))
mauritania_lst = list(map(itemgetter(0), confirmed_data_mauritania.items()))
libya_lst = list(map(itemgetter(0), confirmed_data_libya.items()))

#get last key of confirmed data
algeria_last_key = algeria_lst[-1]
tunisia_last_key = tunisia_lst[-1]
egypt_last_key = egypt_lst[-1]
mauritania_key = mauritania_lst[-1]
libya_last_key = libya_lst[-1]

#get last updated value of confirmed cases
confirmed_cases_algeria = confirmed_data_algeria[algeria_last_key]
confirmed_cases_tunisia = confirmed_data_tunisia[tunisia_last_key]
confirmed_cases_egypt = confirmed_data_egypt[egypt_last_key]
confirmed_cases_mauritania = confirmed_data_mauritania[mauritania_key]
confirmed_cases_libya = confirmed_data_libya[libya_last_key]

#override old values
json_countries['data']['countries'][0]['confirmed'] = int(confirmed_cases_algeria)
json_countries['data']['countries'][1]['confirmed'] = int(confirmed_cases_tunisia)
json_countries['data']['countries'][2]['confirmed'] = int(confirmed_cases_egypt)
json_countries['data']['countries'][3]['confirmed'] = int(confirmed_cases_mauritania)
json_countries['data']['countries'][4]['confirmed'] = int(confirmed_cases_libya)

#**************************DEATHS CASES PARSING*****************************#

#Get deaths data for each country
deaths_data_algeria = json.dumps(deaths_data[2])
deaths_data_tunisia = json.dumps(deaths_data[212])
deaths_data_egypt = json.dumps(deaths_data[98])
deaths_data_mauritania = json.dumps(deaths_data[156])
deaths_data_libya = json.dumps(deaths_data[239])

#load deaths data for each country
deaths_data_algeria = json.loads(deaths_data_algeria)
deaths_data_tunisia = json.loads(deaths_data_tunisia)
deaths_data_egypt = json.loads(deaths_data_egypt)
deaths_data_mauritania = json.loads(deaths_data_mauritania)
deaths_data_libya = json.loads(deaths_data_libya)

#get list of keys for deaths data
algeria_lst = list(map(itemgetter(0), deaths_data_algeria.items()))
tunisia_lst = list(map(itemgetter(0), deaths_data_tunisia.items()))
egypt_lst = list(map(itemgetter(0), deaths_data_egypt.items()))
mauritania_lst = list(map(itemgetter(0), deaths_data_mauritania.items()))
libya_lst = list(map(itemgetter(0), deaths_data_libya.items()))

#get last key of deaths data
algeria_last_key = algeria_lst[-1]
tunisia_last_key = tunisia_lst[-1]
egypt_last_key = egypt_lst[-1]
mauritania_key = mauritania_lst[-1]
libya_last_key = libya_lst[-1]

#get last updated value of deaths cases
deaths_cases_algeria = deaths_data_algeria[algeria_last_key]
deaths_cases_tunisia = deaths_data_tunisia[tunisia_last_key]
deaths_cases_egypt = deaths_data_egypt[egypt_last_key]
deaths_cases_mauritania = deaths_data_mauritania[mauritania_key]
deaths_cases_libya = deaths_data_libya[libya_last_key]

#override old values
json_countries['data']['countries'][0]['deaths'] = int(deaths_cases_algeria)
json_countries['data']['countries'][1]['deaths'] = int(deaths_cases_tunisia)
json_countries['data']['countries'][2]['deaths'] = int(deaths_cases_egypt)
json_countries['data']['countries'][3]['deaths'] = int(deaths_cases_mauritania)
json_countries['data']['countries'][4]['deaths'] = int(deaths_cases_libya)

#**************************RECOVERED CASES PARSING*****************************#

#Get recovered data for each country
recovered_data_algeria = json.dumps(recovered_data[2])
recovered_data_tunisia = json.dumps(recovered_data[212])
recovered_data_egypt = json.dumps(recovered_data[90])
recovered_data_mauritania = json.dumps(recovered_data[152])
recovered_data_libya = json.dumps(recovered_data[143])

#load recovered data for each country
recovered_data_algeria = json.loads(recovered_data_algeria)
recovered_data_tunisia = json.loads(recovered_data_tunisia)
recovered_data_egypt = json.loads(recovered_data_egypt)
recovered_data_mauritania = json.loads(recovered_data_mauritania)
recovered_data_libya = json.loads(recovered_data_libya)

#get list of keys for recovered data
algeria_lst = list(map(itemgetter(0), recovered_data_algeria.items()))
tunisia_lst = list(map(itemgetter(0), recovered_data_tunisia.items()))
egypt_lst = list(map(itemgetter(0), recovered_data_egypt.items()))
mauritania_lst = list(map(itemgetter(0), recovered_data_mauritania.items()))
libya_lst = list(map(itemgetter(0), recovered_data_libya.items()))

#get last key of recovered data
recovered_last_key = algeria_lst[-1]
recovered_last_key = tunisia_lst[-1]
recovered_last_key = egypt_lst[-1]
recovered_key = mauritania_lst[-1]
recovered_key = libya_lst[-1]

#get last updated value of recovered cases
recovered_cases_algeria = recovered_data_algeria[algeria_last_key]
recovered_cases_tunisia = recovered_data_tunisia[tunisia_last_key]
recovered_cases_egypt = recovered_data_egypt[egypt_last_key]
recovered_cases_mauritania = recovered_data_mauritania[mauritania_key]
recovered_cases_libya = recovered_data_libya[libya_last_key]

#override old values
json_countries['data']['countries'][0]['recovered'] = int(recovered_cases_algeria)
json_countries['data']['countries'][1]['recovered'] = int(recovered_cases_tunisia)
json_countries['data']['countries'][2]['recovered'] = int(recovered_cases_egypt)
json_countries['data']['countries'][3]['recovered'] = int(recovered_cases_mauritania)
json_countries['data']['countries'][4]['recovered'] = int(recovered_cases_libya)

#create and write json output file
f = open("output.json", "w")
json_countries = json.dump(json_countries, f, indent=4, sort_keys=True, ensure_ascii=False)
f.close()
