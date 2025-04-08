import matplotlib.pyplot as plt

# Data
data = [7, 8, 5, 6, 7, 8, 7, 6, 5, 9, 8, 6, 7, 8, 9, 7]

# Creating the boxplot
plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor="lightblue"))

# Adding title and labels
plt.title("Boxplot Example")
plt.xlabel("Category")
plt.ylabel("Values")

# Display the plot
plt.show()
