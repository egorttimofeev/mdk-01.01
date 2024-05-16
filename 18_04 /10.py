import pandas as pd

data = {'Имя': ['Егор', 'Полина', 'Ника'],
        'Возраст': [35, 30, 35],
        'Город': ['Самара', 'Ростов', 'Омск']}

df = pd.DataFrame(data)
print(df)