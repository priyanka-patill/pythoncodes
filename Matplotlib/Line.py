import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Creating the plot
plt.plot(x, y,marker='s',ms='10', color='red',mfc='blue', label='Line 1')

# Adding title and labels
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Adding a legend
plt.legend()

# Display the plot
plt.show()
