import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
from pandas import DataFrame

df = pd.read_csv('cv1-1-1.csv')
print(df)

df = pd.read_csv('cv1-1-1.csv',sep=',')

columns_df = df[['0','3']]
print(type(columns_df))
print(columns_df.head())
print(columns_df.tail())

columns_df = df[['0','4']]
print(type(columns_df))
print(columns_df.head())
print(columns_df.tail())

columns_df = df[['3','4']]
print(type(columns_df))
print(columns_df.head())
print(columns_df.tail())

df.head()

df.hist()

df1 = np.loadtxt('cv1-1-1.csv', delimiter=',')
print(df1[0][0])

columns_df1 = df[['0']]
columns_df2 = df[['4']]

x = [columns_df1]
y = [columns_df2]

plt.figure(figsize=(400, 400))
plt.plot(x, y)

plt.xlabel('Ret.Time')
plt.ylabel('Height')

plt.title('Ret.Time and Height')

plt.show()
