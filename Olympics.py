import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

athletes = pd.read_csv('athlete_events.csv')
# print(athletes.head(10))
region = pd.read_csv('noc_regions.csv')
# print(region.head(10))
athletes_df = athletes.merge(region, how='left', on = 'NOC')
# print(athletes_df.head(10))
# print(athletes_df.shape)
athletes_df.rename(columns={'region': 'Region', 'notes':'Notes'}, inplace=True)
# print(athletes_df.info())
# print(athletes_df.describe())
# print(athletes_df.isnull().sum())
nan_values = athletes_df.isna()
nan_col = nan_values.any()
# print(nan_col)            # SHOWS THE COLUMN NAME WETHER THE COL CONTAINS NAN VALUES OR NOT

# QUE - Col names containing null values inform of a list
# print(nan_col[nan_col == 'True'])
athletes_list = athletes_df.columns[nan_col]
# print(athletes_list.tolist())
# print(athletes_df[athletes_df['Team'] == 'India'])
top_10 = athletes_df.Team.value_counts().sort_values(ascending=False)
# print(top_10)
winter_season = athletes_df[athletes_df['Season'] == 'Winter']['Sport'].unique()
# print(winter_season)
summer_season = athletes_df[athletes_df['Season'] == 'Summer']['Sport'].unique()
# print(summer_season)

gender_count = athletes_df.Sex.value_counts()
# print(gender_count)

total_medals = athletes_df.Medal.value_counts()
# print(total_medals)

total_female = athletes_df[(athletes_df['Sex']=='F') & (athletes_df['Season'] == 'Summer')][['Sex','Year']]
total_female_participants = total_female.groupby('Year').count().reset_index()
# print(total_female_participants)

gold_medals = athletes_df[(athletes_df['Medal'] == 'Gold') & (athletes_df['Age'] > 60)][['Name','Sex','Age','Medal']]
# print(gold_medals)

country_gold = athletes_df[athletes_df['Medal'] == 'Gold']['Team']
# print(country_gold.value_counts())

rio_olympics = athletes_df[(athletes_df['Season']=='Summer') & (athletes_df['Year'] == 2016) & (athletes_df['Medal'] == 'Gold')]
# year = rio_olympics.groupby('Year',ascending=False)
print(rio_olympics['Team'].value_counts())