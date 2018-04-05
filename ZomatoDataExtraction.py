import requests
from pprint import pprint
import pandas as pd
from pandas import ExcelWriter


headers = {'Content-Type': 'application/json', 'user-key': '592789033e4cf0e384b54c1ec424c706'}
offset = 0
restaurantNameList = []
ratingList = []
ratingTextList = []
votesList = []
while offset < 100:
	url = 'https://developers.zomato.com/api/v2.1/search?entity_id=306&entity_type=city&start='+str(offset)+'&count=20'
	Response = requests.get(url , headers=headers)
	offset += 20
	Response_Json = Response.json()
	Array_length = Response_Json['restaurants']
	for i in range(len(Array_length)):
		restaurantNameList.append(Response_Json['restaurants'][i]['restaurant']['name'])
		ratingList.append(Response_Json['restaurants'][i]['restaurant']['user_rating']['aggregate_rating'])
		ratingTextList.append(Response_Json['restaurants'][i]['restaurant']['user_rating']['rating_text'])
		votesList.append(Response_Json['restaurants'][i]['restaurant']['user_rating']['votes'])	
df = pd.DataFrame({'Restaurant Name':restaurantNameList,'Rating':ratingList, 'Rating Text':ratingTextList, 'Votes':votesList})
writer = pd.ExcelWriter('Data.xlsx' , engine='xlsxwriter')
df.to_excel(writer,'Sheet1',index=False)
writer.save()
