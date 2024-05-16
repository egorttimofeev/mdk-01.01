import pandas as pd
import numpy as np

data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
df = pd.DataFrame(data, columns=['А', 'Б', 'В'])
print(df)