import pandas as pd

dataframe = pd.DataFrame({'Выручка': [134500, 200670, 300345], 'Затраты': [40450, 50450, 60450]})

# выводим средние значения для столбцов
print(dataframe.mean())