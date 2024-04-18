import pandas as pd

dataframe = pd.DataFrame({'Apple': [1034, 1245, 3985], 'Nvidia': [4034, 5124, 6723]})
print(dataframe.min())  # минимальные значение в столбцах
print(dataframe.max())  # максимальные значения в столбцах