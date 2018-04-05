import requests
from pprint import pprint

headers = {'Content-Type': 'application/json', 'user-key': '592789033e4cf0e384b54c1ec424c706'}

offset = 0
resultSet = []
while offset < 100:
	url = 'https://developers.zomato.com/api/v2.1/search?entity_id=306&entity_type=city&start='+str(offset)+'&count=20'
	Response = requests.get(url , headers=headers)
	offset += 20
	Response_Json = Response.json()
	Array_length = Response_Json['restaurants']
	for i in range(len(Array_length)):
		print(Response_Json['restaurants'][i]['restaurant']['name'])
