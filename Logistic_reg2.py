import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('excel/advertising.csv')
# print(df.head())
# df['Age'].plot.hist(bins=20)
# plt.show()

X = df[['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage','Male']]
y = df['Clicked on Ad']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2 , random_state=101)
reg = linear_model.LogisticRegression()
reg.fit(X_train,y_train)
# print(reg.predict(X_test))
reg1 = reg.predict(X_test)
# print('Score=',reg.score(X_test,y_test))

print(classification_report(y_test,reg1))
print(confusion_matrix(y_test,reg1))


