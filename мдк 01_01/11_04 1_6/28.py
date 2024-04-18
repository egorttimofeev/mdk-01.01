import pandas as pd

dataframe = pd.DataFrame({'Выручка': [105600, 209800, None, 403450],
                          'Убытки': [5034, None, 17093, 80666],
                          'Накладные расходы': [15000, None, 17000, 18000]})

# заполняем пропущенные значения нулями
filled_dataframe = dataframe.fillna(0)
print(filled_dataframe)