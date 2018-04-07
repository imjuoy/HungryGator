import pandas as pd

df = pd.read_csv('TripAdvisor_Data.csv')
df_Miami_Data = df[(df["Country"]=="United States")& (df["City"]=="Miami")]
df_result = df_Miami_Data[["Name","Ranking","Rating","Total Review"]]
print(df_result)
