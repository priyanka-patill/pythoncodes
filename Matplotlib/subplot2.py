import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x)



# First subplot
plt.subplot(2,2,1)
plt.plot(x, y1, color='blue')
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Second subplot
plt.subplot(2,2,2)
plt.plot(x, y2, color='red')
plt.title("cosine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")


# Third subplot
plt.subplot(2,2,3)
plt.plot(x, y3, color='green')
plt.title("Tangent Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")


# Fourth subplot
plt.subplot(2,2,4)
plt.plot(x, y4, color='purple')
plt.title("Exponential decay")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
