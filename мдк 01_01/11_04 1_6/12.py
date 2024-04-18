import pandas as pd

series1 = pd.Series([1, 2, 3], name='XL')
series2 = pd.Series([4, 5, 6], name='M')
df = pd.DataFrame({series1.name: series1, series2.name: series2})
print(df)