import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('excel/911.csv')
# print(data.head())

nan = df.isna()
# print(nan)

col_nan = nan.any()
# print(col_nan)

new_list = df.columns[col_nan]
# print(new_list)

# print(df.zip.value_counts().head(5))      # TOP 5 ZIP CODES

# print(df.twp.value_counts().head())

# print(df.title.nunique())


df['Reason'] = df.title.apply(lambda title : title.split(':')[0])
# print(df.head(7))

# print(df.Reason.value_counts())

sns.countplot(x='Reason', data=df)
# plt.show()
# print(type(df['timeStamp'].iloc[0]))        #str
# print(type(df['timeStamp']))                #<class 'pandas.core.series.Series'>

df.timeStamp = pd.to_datetime(df.timeStamp)
# print(type(df['timeStamp'].iloc[0]))         #<class 'pandas._libs.tslibs.timestamps.Timestamp'>

# print(df.timeStamp.head())

time = df.timeStamp.iloc[0]

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
# print(df.Hour.head(10))
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
# print(df.Month.head())
df['Day_of_week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
# print(df.Day_of_week.head())

# print(df.head(3))

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thur',4:'Fri',5:'Sat',6:'Sun'}
df.Day_of_week = df.Day_of_week.map(dmap)
# print(df.head())

# sns.countplot(x='Day_of_week', data=df, hue='Reason')
# sns.countplot(x='Month', data=df, hue='Reason')
# plt.show()

byMonth = df.groupby('Month').count()
# print(byMonth.head())

byMonth['lat'].plot()
plt.show()