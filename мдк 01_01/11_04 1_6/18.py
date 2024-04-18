import pandas as pd

# создаем DataFrame
dataframe = pd.DataFrame({'Велосипеды': [100, 200, 350], 'Самокаты': [240, 500, 650]})

print(dataframe.loc[0, 'Велосипеды'])  # выводим значение в первой строке и столбце 'Велосипеды'
print(dataframe.loc[1])  # выводим вторую строку целиком
print(dataframe.loc[:, 'Самокаты'])  # выводим столбец 'Самокаты' целиком