import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30],
    'City': ['New York', 'Los Angeles']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Adding a single row to the DataFrame
new_row = {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
df = df.concat(new_row, ignore_index=True)

print("\nDataFrame after adding a single row:")
print(df)

# Adding multiple rows to the DataFrame
new_rows = [
    {'Name': 'David', 'Age': 40, 'City': 'Houston'},
    {'Name': 'Eve', 'Age': 28, 'City': 'Miami'}
]
df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)

print("\nDataFrame after adding multiple rows:")
print(df)
