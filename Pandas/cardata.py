import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Toyota.csv')
print(df)

# Task i: Scatter plot between Age and Price
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['Price'], alpha=0.7, c='blue')
plt.title('Scatter Plot of Age vs Price')
plt.xlabel('Age of Car (in years)')
plt.ylabel('Price of Car')
plt.grid(True)
plt.show()

# Task ii: Histogram of kilometers driven
plt.figure(figsize=(8, 6))
plt.hist(df['KM'], bins=20, color='green', edgecolor='black', alpha=0.7)
plt.title('Histogram of Kilometers Driven')
plt.xlabel('Kilometers Driven')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--')
plt.show()

# Task iii: Bar plot of cars by fuel type
fuel_type_counts = df['FuelType'].value_counts()
plt.figure(figsize=(8, 6))
fuel_type_counts.plot(kind='bar', color=['orange', 'blue', 'green'])
plt.title('Distribution of Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Number of Cars')
plt.xticks(rotation=0)
plt.show()

# Task iv: Pie chart for percentage distribution of cars by fuel type
plt.figure(figsize=(8, 8))
fuel_type_counts.plot(kind='pie', autopct='%1.3f%%', colors=['orange', 'blue', 'green'], startangle=90)
plt.title('Percentage Distribution of Cars by Fuel Type')
plt.ylabel('')  # To avoid displaying "FuelType" as ylabel
plt.show()

# Task v: Box plot of car prices across fuel types
plt.figure(figsize=(8, 6))
df.boxplot(column='Price', by='FuelType', grid=False, patch_artist=True,
           boxprops=dict(facecolor='lightblue', color='blue'),
           medianprops=dict(color='red'))
plt.title('Distribution of Car Prices Across Different Fuel Types')
plt.suptitle('')  # Remove default Pandas boxplot title
plt.xlabel('Fuel Type')
plt.ylabel('Price')
plt.show()
