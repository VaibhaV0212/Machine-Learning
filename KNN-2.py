import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('excel/KNN_Project_data.csv', index_col=0)
# print(df.head())

# sns.pairplot(df, hue="TARGET CLASS")
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))
scaled_feature = scaler.transform(df.drop('TARGET CLASS', axis='columns'))
# print(scaled_feature)  #gives the remaining distance

df_feat = pd.DataFrame(scaled_feature, columns=df.columns[:-1])
# print(df_feat.head())

X = df_feat
y = df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3 , random_state=101)

knn = KNeighborsClassifier(n_neighbors=37)
knn.fit(X_train,y_train)
pred = knn.predict(X_test)
scre = knn.score(X_test,y_test)
# print(pred, '\n',scre)

# print(classification_report(y_test,pred))
# print(confusion_matrix(y_test,pred))

error_rate = []
for i in range(1,60):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10,6))
plt.plot(range(1,40), error_rate, color='Blue', linestyle='dashed', marker='o',
             markerfacecolor='red', markersize=10)
# plt.show()

#re-train with new K value
knn = KNeighborsClassifier(n_neighbors=30)
knn.fit(X_train,y_train)
pred = knn.predict(X_test)
print(classification_report(y_test,pred))
print(confusion_matrix(y_test,pred))
