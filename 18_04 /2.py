import pandas as pd

data = [35000, 6000, 3000, 2000]
labels = ['Ноутбуки', 'Мониторы', 'Принтеры', 'Клавиатуры']

series = pd.Series(data, index=labels)

# выводим значение 3000, обращаясь к элементу с меткой 'Принтеры'
print(series['Принтеры'])