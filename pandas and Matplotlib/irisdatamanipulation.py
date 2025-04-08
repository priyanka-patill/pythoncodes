import pandas as pd

# Load the dataset
df = pd.read_csv('iris.csv')

# Task i: Read the first 8 rows
first_8_rows = df.head(8)
print("First 8 rows of the dataset:")
print(first_8_rows)

# Task ii: Display the column names
column_names = df.columns
print("\nColumn names of the Iris dataset:")
print(column_names)

# Task iii: Fill any missing data with the mean value of the respective column
df_filled = df.fillna(df.mean(numeric_only=True))
print("\nDataset after filling missing values with the mean:")
print(df_filled)

# Task iv: Remove rows that contain any missing values
df_no_missing = df.dropna()
print("\nDataset after removing rows with missing values:")
print(df_no_missing)

# Task v: Group the data by the species of the flower
grouped_by_species = df.groupby('species')
print("\nData grouped by species:")
for species, group in grouped_by_species:
    print(f"\nSpecies: {species}")
    print(group)

# Task vi: Calculate and display the mean, minimum, and maximum values of the Sepal length column
mean_sepal_length = df['sepal_length'].mean()
min_sepal_length = df['sepal_length'].min()
max_sepal_length = df['sepal_length'].max()

print("\nStatistics for Sepal Length:")
print(f"Mean: {mean_sepal_length}")
print(f"Minimum: {min_sepal_length}")
print(f"Maximum: {max_sepal_length}")
