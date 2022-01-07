import numpy as np
import pandas as pd
from sklearn import linear_model
import math
from word2number import w2n

df = pd.read_csv('salary.csv')


new_test_score= math.floor(df['test_score'].median())
df['test_score'] = df.test_score.fillna(new_test_score)

df.experience = df.experience.fillna('zero')

df.experience = df.experience.apply(w2n.word_to_num)
# print(df)

reg = linear_model.LinearRegression()
reg.fit(df[['experience','test_score','interview_score']],df.salary)
print('Salary of =',reg.predict([[2,9,6]]))
print('Salary of =',reg.predict([[12,10,10]]))

