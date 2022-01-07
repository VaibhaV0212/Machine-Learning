import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import math

df = pd.read_csv('excel/loan_data.csv')
# print(df.head(7))
# print(df.value_counts())
# print(df.columns)

# print(df.isna().any())
cat_feats = ['purpose']
final_data = pd.get_dummies(df, columns=cat_feats, drop_first=True)
# print(final_data.head(2))
X = final_data.drop('not.fully.paid',axis='columns')
y = final_data['not.fully.paid']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
reg = tree.DecisionTreeClassifier()
reg.fit(X_train,y_train)
pred = reg.predict(X_test)
scre = reg.score(X_test,y_test)
# print(df.isna().any())
print(scre)

rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train,y_train)
rfc_pred = rfc.predict(X_test)
scre1 = rfc.score(X_test,y_test)
print('Score is',round(scre1,4))
