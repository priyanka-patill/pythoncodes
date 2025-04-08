import pandas as pd
x=['a','b','c','d']
y=pd.Series(x)
print(y)

y=pd.Series(x, index=['1', '2', '3','4'])
print(y)
