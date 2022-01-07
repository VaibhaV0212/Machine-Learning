import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

cancer = load_breast_cancer()
# print(cancer.feature_names)
# print(cancer.keys())

df_cancer = pd.DataFrame(np.c_[cancer['data'], cancer['target']], columns= np.append(cancer['feature_names'],['target']))
# print(df_cancer.head())

# sns.pairplot(df_cancer, hue='target')
sns.countplot(df_cancer['target'])
# plt.show()

X = df_cancer.drop(['target'],axis=1)
y = df_cancer.target
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2 , random_state=5)

svc_model = SVC()
svc_model.fit(X_train,y_train)
# print('Prediction=', svc_model.predict(X_test))
pred =  svc_model.predict(X_test)
print('Score=', svc_model.score(X_test,y_test))
print(classification_report(y_test,pred))
print(confusion_matrix(y_test,pred))
