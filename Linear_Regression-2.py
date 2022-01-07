import numpy as np
import pandas as pd
from sklearn import linear_model

df = pd.read_csv('canada_per_capita_income.csv')
print(df.head(3))

reg = linear_model.LinearRegression()
reg.fit(df[['year']], df['income'])
print(reg.predict([[2020]]))

