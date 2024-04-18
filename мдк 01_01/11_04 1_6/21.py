import pandas as pd

dataframe = pd.DataFrame({'Возраст': [22, 25, 27], 'Зарплата': [70000, 90000, 12000]})
print(dataframe.iat[0, 1])  # выводим значение в первой строке и втором столбце