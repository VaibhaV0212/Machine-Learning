import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import math

df = pd.read_csv('excel/titanic_new.csv')
# print(df.head())

inputs = df[['Pclass','Sex','Age','Fare']]
# print(inputs)

# missing = inputs.isna().sum()
# print(missing)

median_age = math.floor(inputs.Age.median())
# print(mean_age)

inputs['Age'] = inputs['Age'].fillna(median_age)

missing = inputs.isna().sum()
# print(missing)

# print(inputs.describe())
# print()
# print(inputs.describe(include='all'))

new = pd.get_dummies(inputs['Sex'])
# print(new.head(10))

rel_df = pd.concat([inputs, new],axis = 'columns')
# print(rel_df)

final_df = rel_df.drop(['Sex','Fare'] ,axis = 'columns')
print(final_df.head())
