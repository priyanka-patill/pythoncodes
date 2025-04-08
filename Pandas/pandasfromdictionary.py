import pandas as pd

data = {'name': ['nick', 'david', 'joe', 'ross'],'age': ['5', '10', '7', '6']}
data = pd.DataFrame.from_dict(data)
print(data)
