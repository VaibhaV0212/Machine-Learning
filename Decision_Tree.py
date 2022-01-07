import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import tree


df = pd.read_csv('salaries1.csv')
# print(df.head())

inputs = df.drop('salary_more_than_100k', axis='columns')
target = df['salary_more_than_100k']

# dummies = pd.get_dummies(inputs['company'])
# print(dummies)

le_company = LabelEncoder()
le_job = LabelEncoder()
le_course = LabelEncoder()


inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['course_n'] = le_course.fit_transform(inputs['course'])
# print(inputs)

new_df = inputs.drop(['company','job','course'], axis='columns')
# print(new_df)

X = new_df
y = target

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)


reg = tree.DecisionTreeClassifier()
# reg.fit(new_df, target)
# print(reg.predict([[2,2,1]]))
# print(reg.score(new_df, target))

reg.fit(X_train,y_train)
print('Prediciton -',reg.predict(X_test))
print('Score is=',reg.score(X_test,y_test))