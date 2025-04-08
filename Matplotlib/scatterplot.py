import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [40, 16, 27, 38, 10]
c=[ 'r','g','b','y','m']
size=[150,100,200,100,150]

# Creating the scatter plot
#plt.scatter(x, y, color='green', marker='o', label='Data Points')
#plt.scatter(x, y, color=c, marker='o', label='Data Points', s=size, alpha=0.8)
plt.scatter(x, y, color=c, marker='*', label='Data Points', s=size, alpha=0.8)

# Adding title and labels
plt.title("Scatter Plot Example",fontsize=15)
plt.xlabel("X-axis",fontsize=15)
plt.ylabel("Y-axis",fontsize=15)

# Adding a legend
#plt.legend()

# Display the plot
plt.show()
