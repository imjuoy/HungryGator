import requests
from pprint import pprint

headers = {'Content-Type': 'application/json', 'user-key': '592789033e4cf0e384b54c1ec424c706'}

offset = 0

Response = requests.get('https://developers.zomato.com/api/v2.1/search?entity_id = 306&entity_type = city' , headers=headers)

Response_Json = Response.json()

Array_length = Response_Json['restaurants']

print(len(Array_length))

for i in range(len(Array_length)):

	print(Response_Json['restaurants'][i]['restaurant']['name'])
