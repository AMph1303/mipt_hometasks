import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#Task 4 
papers = pd.read_csv('papers001.csv', sep =';')
links = pd.read_csv('links001.csv', sep =';')
res = papers.merge(links, right_on='reference', left_on='title', how='outer')
res=res[merged['author'].isna()==False]
res['referened']=(res['paper_id'].isna()==False).astype(int)
res.drop(columns=['reference', 'id', 'paper_id'],  inplace=True)
res = (res.groupby([res.author, res.title], sort=False)
         .agg({'referened':'sum'})
         .reset_index())
res = round(res.groupby(by = 'author').mean(),3)
res.sort_values(by=['referened'], ascending=False, inplace=True)
print(res.head(3))


