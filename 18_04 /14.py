import pandas as pd

# Чтение данных из файла CSV
dataframe = pd.read_csv('/Users/egorttimofeev/GitHub/pandas/example/data.csv')

# Вывод первых 2 строк DataFrame
print(dataframe.head(2))

# Вывод последних 2 строк DataFrame
print(dataframe.tail(2))