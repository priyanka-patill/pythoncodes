import pandas as pd

# define a dictionary containing student data
data = {'Name': ['John', 'Emma', 'Michael', 'Sophia'],
        'Height': [5.5, 6.0, 5.8, 5.3],
        'Qualification': ['BSc', 'BBA', 'MBA', 'BSc']}

# convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# declare a new list
address = ['New York', 'London', 'Sydney', 'Toronto']

# assign the list as a column
df['Address'] = address

#print(df)
#print(df.shape)
#print(df.columns)
#print(df.Address)
#print(df.dtypes)
#x=(df.values)
#print(x)
#print(df.index)
# Filtering 
y=df[df['Height']>5.5]
print(y)





