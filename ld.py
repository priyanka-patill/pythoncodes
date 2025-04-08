# List of values
a = [10, 20, 30]

# Convert to dictionary with index as key and value as value
b = {index: value for index, value in enumerate(a)}
print(b)

#Output:{0: 10, 1: 20, 2: 30}

a= ["a", 1, "b", 2, "c", 3]

# Create dictionary by pairing elements, using every second element as value
result = {a[i]: a[i + 1] for i in range(0, len(a), 2)}
print(result)  

#Output={'a': 1, 'b': 2, 'c': 3}

a = ["apple", "banana", "cherry"]

# Create dictionary where each fruit is a key, and its length is the value
b = {value: len(value) for value in a}

print(b)  

#Output:{'apple': 5, 'banana': 6, 'cherry': 6}

