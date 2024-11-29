import pandas as pd

df = pd.read_csv('votes by city.csv')

print(df.head)
print(df.info())
print(df.describe())

#print(df[['city', 'SUM of votes']])
#print(df.loc[2784])
#print(df.loc[2784,'city'])
#print(df[df['SUM of votes']>100])

df = pd.read_csv('dz.csv')
print(df.head)

group = df.groupby('City')['Salary'].mean()
print(group)

