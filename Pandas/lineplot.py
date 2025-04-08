"""
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot
plt.plot(x, y)

# Add a title and labels
plt.title('Sample Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()
"""
import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 4]

# Create a bar plot
plt.bar(categories, values)

# Add a title and labels
plt.title('Sample Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

# Display the plot
plt.show()
