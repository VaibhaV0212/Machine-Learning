import pandas as pd
import numpy as np

df = pd.read_csv('excel/pokemon.csv')
# print(df.head(6))
# print(df.columns)
# print(df.Name)                   #columns
# print(df.iloc[1])                  #rows
# print(df.iloc[2:3,1:2])
# print(df.loc[df['Type 1' == 'Fire'])
# print(df.describe())
sorting = df.sort_values('Name',ascending=False)
# print(sorting)
# df['total_power'] =df['HP'] + df['Attack']+ df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']               # 1st way
# df['total'] = df.iloc[:,4:9].sum(axis=1)                                                                              # 2nd way

cols = (df.columns)
df = df[cols[0:4] + [cols['Total']] + cols[4:10]]
print(df)


