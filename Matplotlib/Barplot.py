import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]
c=['red','blue','green','skyblue']
# Creating the bar plot
plt.bar(categories, values,width=0.4, color=c)

# Adding title and labels
plt.title("Bar Plot Example")
plt.xlabel("Categories")
plt.ylabel("Values")

# Display the plot
plt.show()
