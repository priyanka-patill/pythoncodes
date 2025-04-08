# List of tuples
data = [(3, 'apple'), (1, 'banana'), (2, 'cherry'), (4, 'date')]
# Bubble sort algorithm to sort the list of tuples
n = len(data)
for i in range(n):
    for j in range(0, n-i-1):
        # Compare the first element of each tuple
        if data[j][0] > data[j+1][0]:
            # Swap if the element is greater
            data[j], data[j+1] = data[j+1], data[j]

print(data)  # Output: [(1, 'banana'), (2, 'cherry'), (3, 'apple'), (4, 'date')]
