import pandas as pd

# создаем Series из списка
data1 = [10, 20, 30, 40, 50]
series1 = pd.Series(data1)

# создаем Series из словаря
data2 = {'А': 10, 'Б': 20, 'В': 30, 'Г': 40, 'Д': 50}
series2 = pd.Series(data2)

print(series1)
print(series2)