import pandas as pd

# создание DataFrame
dataframe = pd.DataFrame({'M': [100, 120, 130], 'L': [140, 150, 165]})

# запись данных в файл CSV
dataframe.to_csv('/Users/egorttimofeev/GitHub/pandas/example/output.csv', index=False)