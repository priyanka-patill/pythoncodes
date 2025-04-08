
import matplotlib.pyplot as plt

# Data
data = [7, 8, 5, 6, 7, 8, 7, 6, 5, 9, 8, 6, 7, 8, 9, 7]

# Creating the histogram using pyplot
plt.hist(data, bins=5, color='blue', edgecolor='black', alpha=0.7)

# Adding title and labels
plt.title("Histogram using Pyplot")
plt.xlabel("Bins")
plt.ylabel("Frequency")

# Display the plot
plt.show()
