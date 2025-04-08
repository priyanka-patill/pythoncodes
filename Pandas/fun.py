import pandas as pd

# create a dataframe
data = {'Name': ['John', 'Alice', 'Bob', 'Emma', 'Mike', 'Sarah', 'David', 'Linda', 'Tom', 'Emily'],
        'Age': [25, 30, 35, 28, 32, 27, 40, 33, 29, 31],
        'City': ['New York', 'Paris', 'London', 'Sydney', 'Tokyo', 'Berlin', 'Rome', 'Madrid', 'Toronto', 'Moscow']}
df = pd.DataFrame(data)
print(df)
# display the first three rows
print('First Three Rows:')
print(df.head(3))
print()

# display the first five rows
print('First Five Rows:')
print(df.head(5))
# display the last three rows
print(df.tail(3))
#Get DataFrame Information
df.info()


