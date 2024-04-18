import pandas as pd

data = [10, 20, 30, 40, 50]
index = ['2019', '2020', '2021', '2022', '2023']
series = pd.Series(data, index=index)
print(series)
print(series['2021'])  # вывод: 30
print(series['2023'])  # вывод: 50