import pandas as pd

dataframe = pd.DataFrame({'A': [12, 25, 3],
                          'B': [41, 55, 16]})

# применяем функцию к каждому элементу DataFrame
processed_dataframe = dataframe.apply(lambda x: x ** 2 + 3 * x - 1)
print(processed_dataframe)

# применяем функцию к одному столбцу DataFrame
processed_dataframe['A'] = processed_dataframe['A'].apply(lambda x: x / 5)
print(processed_dataframe)

# применяем функцию ко второй строке
processed_dataframe.loc[1] = processed_dataframe.loc[1].apply(lambda x: x * 10)
print(processed_dataframe)