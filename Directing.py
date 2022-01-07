import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# fashion_train_data = pd.read_csv('excel/fashion-mnist_train.csv')
# fashion_test_data = pd.read_csv('excel/fashion-mnist_test.csv')
# # print(fashion_test_data.head())

# training = np.array(fashion_train_data, dtype='float64')
# test = np.array(fashion_test_data, dtype='float64')

# print(training.head())
data = pd.read_csv('excel/appdata10.csv')
# print(data.info())
# print(data['hour'].head(10))
data['hour'] = data['hour'].str.slice(1,3).astype(int)
# print(data['hour'].head())
# print(data.columns)
data2 = data.copy().drop(['user','screen_list','first_open','enrolled_date','enrolled'], axis=1)
# print(data2.head())


for i in range(1, data2.shape[1] + 1):
    plt.subplot(3,3,i)
    f = plt.gca()
    f.set_title(data2.columns.values[i-1])

    vals = np.size(data2.iloc[:, i-1].unique())
    plt.hist(data2.iloc[:,i-1], bins= vals,color='red')
    # plt.show()
