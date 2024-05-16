import pandas as pd

dataframe = pd.DataFrame({'Производитель': ['Nestle', 'Hershey', 'Mars', 'Ferrero', 'Cadbury'],
                          'Продукт': ['KitKat', 'Hershey Bar', 'Snickers', 'Ferrero Rocher', 'Dairy Milk'],
                          'Цена': [2.99, 1.99, 1.49, 14.99, 13.49]})

# создаем сводную таблицу
pivot_table_data = dataframe.pivot_table(index='Производитель', columns='Продукт', values='Цена', aggfunc='mean')
print(pivot_table_data)