import numpy as np
import pandas as pd
from sklearn import linear_model
import math

df = pd.read_csv('homeprices_township.csv')
# print(df.head(3))

median_bedrooms = math.floor(df.bedrooms.median())
# print(median_bedrooms)

df.bedrooms = df.bedrooms.fillna(median_bedrooms)
# print(df.head())

reg = linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']], df.price)
print('The price is= ',reg.predict([[3000,3,40]]))
print('The price is= ',reg.predict([[3000,4,15]]))


