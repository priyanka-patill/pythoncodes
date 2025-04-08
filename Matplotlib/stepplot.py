import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Creating the step plot
plt.step(x, y, where='mid', color='orange', label='Step Line')

# Adding title and labels
plt.title("Step Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Adding a legend
plt.legend()

# Display the plot
plt.show()
