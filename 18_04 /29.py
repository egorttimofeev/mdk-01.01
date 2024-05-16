import pandas as pd

dataframe1 = pd.DataFrame({'A': [10, 20, 30, 40],
                           'B': ['XL', 'L', 'M', 'S']})

dataframe2 = pd.DataFrame({'A': [10, 20, 30, 40],
                           'C': ['52', '48', '46', '42']})

# объединяем 2 объекта DataFrame на основе столбца 'A'
merged_dataframe = pd.merge(dataframe1, dataframe2, on='A')
print(merged_dataframe)