import json
import urllib

api_key = open('.api_key').read()

query = raw_input('Enter data \n')

service_url = 'https://kgsearch.googleapis.com/v1/entities:search'

params = {
    'query': query,
    'limit': 1,
    'indent': True,
    'key': api_key,
}

url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())

for element in response['itemListElement']:
    print str(element['result']['name']) + ' ' + str(element['result']['@type'])