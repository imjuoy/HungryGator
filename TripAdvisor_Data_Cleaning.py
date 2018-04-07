##This file should read the data from CSV and then filter ratings, votes and names,etc of restaurants only based out of San Francisco.

import pandas as pd

counter = 0

df = pd.read_csv('TripAdvisor_Data.csv')
Country_Names = df.Country
for i in Country_Names:
	if 'United States' in i:
		counter += 1
print(counter)
