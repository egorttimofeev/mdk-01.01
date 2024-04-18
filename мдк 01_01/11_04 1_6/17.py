import pandas as pd

# создание DataFrame
dataframe = pd.DataFrame({'Москва': [10000000, 250000, 300], 'Самара': [4000000, 150000, 600]})

# запись данных в файл Excel
dataframe.to_excel('/Users/egorttimofeev/GitHub/pandas/example/output.xlsx', index=False)