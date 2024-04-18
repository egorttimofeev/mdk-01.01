import pandas as pd

dataframe = pd.DataFrame({'А': [3, 2, 1], 'Б': [6, 5, 4], 'В': [9, 8, 7]})

# сортируем данные по столбцу 'A'
dataframe_sorted = dataframe.sort_values(by='А')
print(dataframe_sorted)