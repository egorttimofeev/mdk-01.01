import pandas as pd

dataframe = pd.DataFrame({'Ноутбуки': [341, 267, 382], 'Планшеты': [374, 503, 466]})

# выводим суммы значений по столбцам
print(dataframe.sum())