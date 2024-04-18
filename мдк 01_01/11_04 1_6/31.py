import pandas as pd

dataframe = pd.DataFrame({'Лейкоциты': [134, 232, 321], 'Эритроциты': [474, 561, 690]})

# вывод основных статистических показателей
print(dataframe.describe())