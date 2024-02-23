import pandas as pd

path = 'D:\\Imer\\ProgrammingPractice\\Python\\Spark\\sparkIntroduction\\files\\goalsMessiCr7.csv'
dataframe = pd.read_csv(path)

print(dataframe.head())

print(dataframe['Competition'].unique())