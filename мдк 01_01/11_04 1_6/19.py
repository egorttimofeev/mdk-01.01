import pandas as pd

# создаем DataFrame
dataframe = pd.DataFrame({'Кошки': [400, 500, 600], 'Собаки': [145, 255, 350]})

print(dataframe.iloc[0, 1])  # выводим значение в первой строке и втором столбце
print(dataframe.iloc[1])  # выводим вторую строку целиком
print(dataframe.iloc[:, 1])  # выводим второй столбец целиком