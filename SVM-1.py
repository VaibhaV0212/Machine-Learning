import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_iris


iris = load_iris()
# print(dir(iris))
# print(iris.feature_names)

df = pd.DataFrame(iris.data, columns=iris.feature_names)

# print(iris.target)
# print(iris.target_names)
df['target'] = iris.target
df['target_names'] = df.target.apply(lambda x: iris.target_names[x])
# print(df.head())
# print(df[df.target==2])

X = df.drop(['target', 'target_names'], axis=1)
y = df.target

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3 , random_state=101)
reg = SVC(C=30)
reg.fit(X_train,y_train)
print('score=', reg.score(X_test,y_test))



