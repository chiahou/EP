import pandas as pd 

clicks = pd.read_csv('clicks.csv', sep='|', header=0)
clicks = clicks.loc[:, ~clicks.columns.str.match('Unnamed')]
for row, values in clicks.iterrows():
    clicks.loc[0,0] = clicks.loc[0,0].replace(' ','')

games = pd.read_csv('games.csv', sep='|', header=0)
games = games.loc[:, ~games.columns.str.match('Unnamed')]
