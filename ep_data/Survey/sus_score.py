import pandas as pd 
import statistics

data = pd.read_csv('game_sus.csv', sep=",", header=0, encoding="utf-8")
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
data = data.iloc[:,0:12]

data_qs = {}

for index, value in data.iterrows():
    data_qs[value].append(value[index])

print(data_qs)
