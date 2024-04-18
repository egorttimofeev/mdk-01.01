import pandas as pd

dataframe = pd.DataFrame({'Углеводы': [43, 27, None, 49],
                          'Жиры': [50, None, 17, 8],
                          'Белки': [25, 5, 11, None]})

# ищем пропущенные значения
missing_values = dataframe.isnull()
print(missing_values)