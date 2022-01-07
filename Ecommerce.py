import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

df = pd.read_csv('excel/Ecommerce_Customers.csv')
# print(df.head(4))
# print(df.columns)

X = df.drop(['Address','Yearly Amount Spent','Email','Avatar'], axis='columns')
y = df['Yearly Amount Spent']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
reg = linear_model.LinearRegression()
reg.fit(X_train,y_train)
print(reg.predict(X_test))
print('Score=', reg.score(X_test,y_test))


