import requests
import json

from secrets import API_KEY

params = {
	'access_key': API_KEY,
	'base': 'EUR'
}

BASE_URL = f'http://data.fixer.io/api/latest'

response = requests.get(
	BASE_URL,
	params=params
	)

print(json.dumps(response.json(), indent=2))