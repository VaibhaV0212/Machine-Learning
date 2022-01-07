import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://raw.githubusercontent.com/codebasics/py/master/ML/7_logistic_reg/insurance_data.csv')
# print(df.head())

X = df[['age']]
y = df['bought_insurance']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1)

reg = linear_model.LogisticRegression()
reg.fit(X_train, y_train)
print('X_test-', X_test)
print(reg.predict(X_test))
print(reg.score(X_test,y_test))

