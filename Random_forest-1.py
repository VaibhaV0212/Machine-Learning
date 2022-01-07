import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('excel/kyphosis.csv')
# print(df.head(7))

X = df.drop('Kyphosis',axis='columns')
y = df.Kyphosis

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

reg= tree.DecisionTreeClassifier()
reg.fit(X_train,y_train)
pred = reg.predict(X_test)
scre = reg.score(X_test,y_test)
# print(pred ,'/n', scre)
# print(classification_report(y_test,pred))
# print(confusion_matrix(y_test,pred))

rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train,y_train)
pred_rfc = rfc.predict(X_test)
print(pred_rfc ,'/n', scre)
print(classification_report(y_test,pred_rfc))
print(confusion_matrix(y_test,pred_rfc))

