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
totalData = []
urlList = []
addressList = []
while offset < 100:
	url = 'https://developers.zomato.com/api/v2.1/search?entity_id=291&entity_type=city&start='+str(offset)+'&count=20'
	Response = requests.get(url , headers=headers)
	offset += 20
	Response_Json = Response.json()
	Array_length = Response_Json['restaurants']
	for i in range(len(Array_length)):
		totalData.append(Response_Json['restaurants'][i])
		restaurantNameList.append(Response_Json['restaurants'][i]['restaurant']['name'])
		ratingList.append(Response_Json['restaurants'][i]['restaurant']['user_rating']['aggregate_rating'])
		ratingTextList.append(Response_Json['restaurants'][i]['restaurant']['user_rating']['rating_text'])
		votesList.append(Response_Json['restaurants'][i]['restaurant']['user_rating']['votes'])
		urlList.append(Response_Json['restaurants'][i]['restaurant']['url'])
		addressList.append(Response_Json['restaurants'][i]['restaurant']['location']['address'])	
df1 = pd.DataFrame({'AllData':totalData})
df2 = pd.DataFrame({'Restaurant Name':restaurantNameList,'Rating':ratingList, 'Rating Text':ratingTextList, 'Votes':votesList, 'Url':urlList, 'Address': addressList})
writer = pd.ExcelWriter('Data_with_TripAdvisor.xlsx' , engine='xlsxwriter')
df1.to_excel(writer,'Sheet1',index=False)
df2.to_excel(writer,'Sheet2',index=False)
writer.save()
