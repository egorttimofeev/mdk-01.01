import pandas as pd
import numpy as np

# Создание данных для записи
data = {
    'Наименование': ['Продукт1', 'Продукт2'],
    'Цена': [100, 200],
    'Скидка': [10, 20],
    'день окончания': ['2024-05-01', '2024-05-02'],
    'цена за 1 кг/шт': [5, 10]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Создание нового Excel-файла и запись в него данных
with pd.ExcelWriter('/Users/egorttimofeev/Downloads/linia2(1).xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='linia', index=False)
    df.to_excel(writer, sheet_name='X5', index=False)