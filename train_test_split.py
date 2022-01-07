import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://raw.githubusercontent.com/codebasics/py/master/ML/6_train_test_split/carprices.csv')
# print(df)

X = df[['Mileage','Age(yrs)']]
y = df['Sell Price($)']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
# print('X_train-', X_train)
# print('X_test-', X_test)
# print()
# print('y_train-', y_train)
print('y_test=',y_test)

reg = linear_model.LinearRegression()
reg.fit(X_train,y_train)
print(reg.predict(X_test))
print(reg.score(X_test,y_test))
