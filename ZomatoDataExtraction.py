import requests
from pprint import pprint

headers = {'Content-Type': 'application/json', 'user-key': '592789033e4cf0e384b54c1ec424c706'}

Response = requests.get('https://developers.zomato.com/api/v2.1/search?entity_id = 306&entity_typei = city' , headers=headers)

print(Response.json())
