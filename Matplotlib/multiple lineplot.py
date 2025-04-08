import matplotlib.pyplot as plt

# Data for the line plot
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 1, 8, 7]
y2 = [5, 3, 6, 2, 9]

# Create the line plot
plt.plot(x, y1, label='Line 1', marker='o', linestyle='-')
plt.plot(x, y2, label='Line 2', marker='*', linestyle='--')

# Add labels, title, and legend
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Line Plot Example')
plt.legend()

# Show the plot
plt.show()
