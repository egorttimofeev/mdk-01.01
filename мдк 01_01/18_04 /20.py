import pandas as pd

dataframe = pd.DataFrame({'Фрукты': [150, 250, 350], 'Овощи': [420, 520, 625]})
print(dataframe.at[0, 'Фрукты'])  # выводим значение в первой строке и столбце 'Фрукты'