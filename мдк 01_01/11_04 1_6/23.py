import pandas as pd

# создаем DataFrame
dataframe = pd.DataFrame({'А': [1, 2, 3], 'Б': [4, 5, 6], 'В': [4, 5, 6]})

# удаляем столбцы 'A' и 'B'
dataframe_dropped = dataframe.drop(['А', 'В'], axis=1)

print(dataframe_dropped)