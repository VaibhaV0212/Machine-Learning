import pandas as pd
import numpy as np
from sklearn import linear_model 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import metrics

df = pd.read_csv('excel/USA_Housing.csv')
# print(df.head())
# print(df.describe())
# print(df.columns)

X = df.drop(['Price','Address'], axis='columns')
# print(X.head())
y = df.Price
# print(y.head())

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.4 , random_state=101)
reg = linear_model.LinearRegression()
reg.fit(X_train,y_train)
# print(reg.predict(X_test))
# print(reg.score(X_test,y_test))
reg1 = reg.predict(X_test)
plt.scatter(y_test,reg1)
# plt.show()

mae = metrics.mean_absolute_error(y_test, reg1)
mse = metrics.mean_squared_error(y_test, reg1)
rmse = np.sqrt(mse)
rsqrt = explained_variance_score(y_test, predictions)

print('MAE: {} \nMSE: {} \nRMSE: {} \nR-squared: {}'.format(mae, mse, rmse, rsqrt))

