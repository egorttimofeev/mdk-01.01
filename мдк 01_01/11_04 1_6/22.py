import pandas as pd

dataframe = pd.DataFrame({'Завтрак': [100, 20, 35], 'Обед': [40, 50, 65], 'Ужин': [20, 150, 75]})

# получаем размеры DataFrame с помощью shape
print(dataframe.shape)  # выводим (3, 3) - 3 строки и 3 столбца
