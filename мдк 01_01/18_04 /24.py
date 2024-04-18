import pandas as pd

dataframe = pd.DataFrame({'А': [10, 20, 30], 'Б': [45, 55, 65], 'В': [74, 85, 96], 'Г': [94, 35, 66]})

# удаляем строки 0 и 1
dataframe_dropped = dataframe.drop([0, 1], axis=0)

print(dataframe_dropped)