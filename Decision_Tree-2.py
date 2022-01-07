import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import math

df = pd.read_csv('titanic_new.csv')
# print(df.head())

inputs = df[['Pclass','Sex','Age','Fare']]
target = df['Survived']
# print(inputs.head(3))
# print(target.head(4))

new_age = math.floor(df.Age.median())
# print(new_age)
inputs.Age = inputs.Age.fillna(new_age)

le_Sex = LabelEncoder()

inputs['Gender'] = le_Sex.fit_transform(inputs['Sex'])
# print(inputs.head(3))

new_df = inputs.drop('Sex', axis='columns')
# print(new_df.head(3))

reg = tree.DecisionTreeClassifier()
reg.fit(new_df,target)

print('Prediction-',reg.predict([[2,22.0,31.12,1]]))
print('Score-',reg.score(new_df, target))