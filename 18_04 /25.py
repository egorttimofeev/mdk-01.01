import pandas as pd

dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# переименование столбцов 'A' и 'B'
dataframe_renamed = dataframe.rename(columns={'A': 'Столбец_1', 'B': 'Столбец_2'})
print(dataframe_renamed)