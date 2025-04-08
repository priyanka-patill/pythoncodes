import matplotlib.pyplot as plt
import numpy as np
# Data for the multiple bar chart
categories = [' A', ' B', 'C']
group1 = [5, 7, 3]
group2 = [6, 4, 5]
group3 = [4, 6, 4]
x = np.arange(len(categories))
print(x)# Position of bars on the x-axis
bar_width = 0.2  # Width of the bars
# Create the multiple bar chart
plt.bar(x - bar_width, group1, width=bar_width, label='Group 1', color='red')
plt.bar(x, group2, width=bar_width, label='Group 2', color='blue')
plt.bar(x + bar_width, group3, width=bar_width, label='Group 3',color='green')
# Add labels, title, and legend
#plt.xticks(x, categories)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Multiple Bar Chart Example')
plt.legend()
# Show the chart
plt.show()
