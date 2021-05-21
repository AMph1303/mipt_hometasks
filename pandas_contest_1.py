
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#TASK 1
df = pd.DataFrame()
N, M = input().split()
N= int(N)
M= int(M)
for i in range(N):
    df[i] = np.array(input().split(), dtype=np.number)
print(((df<-5).astype(int)).sum().sum())
print(-(df[df<0].sum().sum()))
print(np.max(np.max(df)))



