import matplotlib.pyplot as plt

# Example data
labels = [' A', ' B', ' C', 'D']
sizes = [25, 50, 20, 20]  # Percentages or counts
colors = ['gold', 'lightblue', 'lightgreen', 'salmon']
explode = (0.2, 0, 0, 0)  # Highlight the first slice (Category A)

# Create the pie chart
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=30)
plt.title('Pie Chart Example')
plt.show()
