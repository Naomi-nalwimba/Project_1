#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:23:40 2024

@author: Naomi_Nalwimba
"""

import pandas as pd
#import numpy as np

df = pd.read_csv('/home/avntrainee/Project_One/movie_dataset.csv')
print(df)

#For the uncleaned Data
df_1= pd.read_csv('/home/avntrainee/Project_One/movie_dataset.csv')
print(df)
#To drop empty rows
df.dropna(inplace = True)

#To reset the index
df = df.reset_index(drop=True)


#To drop duplicated data
df.drop_duplicates(inplace = True)
print(df)

#TO see the column titles we have 
df.columns.str.strip()

#To replace empty space with nothing 
df.columns.str.replace(" ", "")

#To see Movie with highest rating
print("\nMaximun rating")
Max_rating=df["Rating"].max()
print(Max_rating)

# For Movie with the highest rating.
print(df['Rating'] == Max_rating)
ans=(df['Rating'] == Max_rating)
print(ans)

print("\nMovie row with highest rating")
print(df[ans])

#To find the average revenue of all movies in the dataset.
print('\nMaximun Revenue(Million)')
print(max(df['Revenue (Millions)']))

Mean_Revenue = df['Revenue (Millions)'].mean()
print('\n')
print(f'The Mean Revenue of all Movies ={Mean_Revenue:.2f} Million')

#To find the he average revenue of movies from 2015 to 2017 in the dataset
print('\n')
Filtered_revenue= df[(df['Year']>=2015) & (df['Year']<=2017)]
Average_Revenue_from_2015_to_2017 = Filtered_revenue['Revenue (Millions)'].mean()
print(f'The average revenue of movies from 2016 to 2017 in the dataset = {Average_Revenue_from_2015_to_2017} Million')


#Number of Movies released in 2016
print(df_1['Year'] ==2016)
Movies_from_2016=(df_1['Year']==2016)
print(len(df_1[Movies_from_2016]))

#To find number of Movies directed by Christopher Nolan

print(df['Director'] == 'Christopher Nolan')
ans = df['Director'] == 'Christopher Nolan'

print(df[ans])
print('\nNumber of movies released by Christopher Nolan')
print(len(df[ans]))


#Number of movies in the dataset with rating of at least 8.0

print(df["Rating"] >= 8.0)
ans = df['Rating'] >= 8.0

print(df[ans])
print('\nMovies with rating of atleast 8.0')
print(len(df[ans]))


#Median rating of movies directed by Christopher Nolan
print('\n')
Movies_Christopher_Nolan = df[df ['Director'] == 'Christopher Nolan']
Median_rating =Movies_Christopher_Nolan ['Rating'].median()
print(f'Meadian rating of movies directed by Christopher Nolan: {Median_rating}')

#Year with the highest average rating
print('\n')
average_ratings=df_1.groupby('Year') ['Rating'].mean()
Highest_average_year = average_ratings.idxmax()
Highest_average_rating = average_ratings.max()
print(f'The year with the highest average rating is {Highest_average_year}')


#The percentage increase in number of movies made between 2006 and 2016
Start=2006
End=2016 
sliced_Start=df_1[df_1[('Year')] == Start] #&(df['Year']==Start)
print(len(sliced_Start))

sliced_End= df_1[(df_1['Year'] == End)] #&(df['Year]==End)
per_increase = ((len(sliced_End)-len(sliced_Start))/len(sliced_Start))*100
print('\nThe percentage increase in number of movies made between 2006 and 2016 is:')
print(per_increase)

#Most common actor
print('\n')
Actor = pd.Series(df["Actors"].str.split(',').sum()).mode()
print('The Most common actor is:'); print(Actor)

#Unique Genre in the dataset
print('\n')
unique_genre = pd.Series(df['Genre'].str.split(',').sum()).unique()
print(f'The Number of movies with unique genres = {len(unique_genre)} genres')























