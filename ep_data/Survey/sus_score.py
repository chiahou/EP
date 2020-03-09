import pandas as pd 
import statistics as st 


'''Clean Data'''

data = pd.read_csv('game_sus.csv', sep=",", header=0, encoding="utf-8")
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
data = data.iloc[:,2:12]

'''Convert negative questions'''



'''Calculate SUS'''

means = []

for label, content in data.items():
	content = pd.to_numeric(content, downcast="float")
	means.append(st.mean(content))

y = 0
for x in means:
	x = x*2.5
	y += x

print(y)


'''Cronbach's Alpha'''




