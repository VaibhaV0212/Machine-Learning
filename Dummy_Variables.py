import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

df = pd.read_csv('town_dummies.csv')
# print(df)

dummies = pd.get_dummies(df.town)
df_dummies = pd.concat([df,dummies], axis = 'columns')
# print(df_dummies)

new_dummies = df_dummies.drop(['town','subhash nagar'], axis='columns')
# print(new_dummies)

X = new_dummies.drop('price', axis='columns')
y = new_dummies['price']
# print('X=',X)
# print('Y=',y)

reg = linear_model.LinearRegression()
reg.fit(X,y)
print(reg.predict([[4000,0,1]]))
print('score is-', reg.score(X,y))