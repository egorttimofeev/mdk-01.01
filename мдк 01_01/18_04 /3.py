import pandas as pd

# создаем MultiIndex с двумя уровнями
index = pd.MultiIndex.from_tuples([('Москва', 'Ноутбуки'), ('Москва', 'Настольные ПК'),
                                   ('Санкт-Петербург', 'Ноутбуки'), ('Санкт-Петербург', 'Настольные ПК')])

# создаем DataFrame с MultiIndex
data = [[1000, 200000], [3000, 400000], [5000, 600000], [7000, 800000]]
df = pd.DataFrame(data, index=index, columns=['Продажи', 'Прибыль'])

print(df)