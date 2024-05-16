import pandas as pd

dataframe = pd.read_csv('data.csv')
series_1 = dataframe['column_name_1']
series_2 = dataframe['column_name_2']
series_3 = dataframe['column_name_3']

print(series_1)
print(series_2)
print(series_3)
