import matplotlib.pyplot as plt
import numpy as np

# Data for placement
years = ['2020', '2021', '2022', '2023']
CSE = [50, 60, 65, 70]
ECE = [30, 40, 50, 55]
IT = [20, 25, 30, 35]
CE = [15, 20, 25, 30]
EE = [10, 15, 20, 25]

# Position of bars on the x-axis
x = np.arange(len(years))

# Creating the stacked bar chart
plt.bar(x, CSE, label='CSE',width=0.2, color='blue')
plt.bar(x, ECE, label='ECE', width=0.2,bottom=CSE, color='green')
plt.bar(x, IT, label='IT', width=0.2,bottom=np.array(CSE)+np.array(ECE), color='orange')
plt.bar(x, CE, label='CE', width=0.2,bottom=np.array(CSE)+np.array(ECE)+np.array(IT), color='purple')
plt.bar(x, EE, label='EE', width=0.2,bottom=np.array(CSE)+np.array(ECE)+np.array(IT)+np.array(CE), color='red')

# Adding labels and title
plt.xlabel('Years')
plt.ylabel('Number of Placements')
plt.title('Placements of Different Branches Over the Years')
plt.xticks(x, years)
plt.legend()

# Show the plot
plt.show()
