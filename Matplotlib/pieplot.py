import matplotlib.pyplot as plt

# Data
labels = ['Apple', 'Banana', 'Cherry', 'Durian']
sizes = [25, 35, 20, 20]
colors = ['red', 'yellow', 'lightcoral', 'skyblue']
explode = (0.1, 0, 0, 0)  # Explode the 1st slice (Apple)
plt.figure(figsize=(10, 7))
# Creating the pie plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Adding title
plt.title("Pie Chart Example")
plt.legend()

# Display the plot
plt.show()
