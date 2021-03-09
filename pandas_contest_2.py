import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#Task 2
X = np.array([0.5, 0.1, 0.5])
A = pd.DataFrame({'1':[0.1, 0, 0,],'2':[0, 0.1, 0],'3':[0, 0, 0.1]}) 
# Тут можно повторить ввод из задачи 1 
#(а вообще, можно было бы тут и без pandas обойтись)
b = np.array([2.5, 2.5, 2.5])
A**=2
print(np.dot(np.dot(X, A),b))

