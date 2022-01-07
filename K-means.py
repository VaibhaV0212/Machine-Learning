import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('excel/Income.csv')
# print(df.head())

plt.scatter(df['Age'], df['Income($)'])
# plt.show()

kn = KMeans(n_clusters=3)
y_pred = kn.fit_predict(df[['Age','Income($)']])
# print(y_pred)

df['cluster'] = y_pred
# print(df.head())

# now plot the new graph
df1 = df[df['cluster']==0]
df2 = df[df['cluster']==1]
df3 = df[df['cluster']==2]
# print(df1)
plt.scatter(df1['Age'], df1['Income($)'],color='green')
plt.scatter(df2['Age'], df2['Income($)'],color='red')
plt.scatter(df2['Age'], df2['Income($)'],color='blue')
# plt.show() # ANOMALY CAME OVER HERE SINCE FEATURES WERE NOT TRAINED PROPERLY

# USE MinMaxScaler ON INCOME COLUMN TO SCALE 2 FEATURES 
scaler = MinMaxScaler()
scaler.fit(df[['Income($)']])  # scale between 0 to 1
df['Income($)'] = scaler.transform(df['Income($)'])
print(df.head(4))
