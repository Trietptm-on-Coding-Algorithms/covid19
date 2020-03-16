import pandas as pd
from statsmodels.regression.linear_model import OLS
import numpy as np

data = pd.read_excel('Italy.xlsx', index_col=0)

y = np.log(data.iloc[:, 0])
y.name = 'Infected cases'
x = data[['max', 'humidity']].sub([15, 75])
x.columns = ['Temp - 15oC', 'Humidity - 75%']
res = OLS(y, x, hasconst=False).fit()
print(res.summary())

data.iloc[-3, 2] = 1
y = np.log(data.iloc[:, 0]/data.iloc[:, 2])
y.name = 'Growth rate'

res = OLS(y, x, hasconst=False).fit()
print(res.summary())


