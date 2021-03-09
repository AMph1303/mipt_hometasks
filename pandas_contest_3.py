import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#Task 3
df = pd.read_csv('games001.csv', sep =';')
rates = pd.read_csv('rates001.csv', sep =';')

ids = np.array(df['id'])
summ = np.array([])
for i in ids:
    summ=np.append(summ, round(rates[rates['id']==i].mean()[1], 3))
df['rating']=summ
df.sort_values(by=['rating'], ascending=False, inplace=True)
print(df[['name', 'rating']].head(3),'\n')
print(df[df['rating']>8.0].groupby(by = 'company').size().head(1))



