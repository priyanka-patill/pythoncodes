# Lambda function to add two numbers
add = lambda x, y: x + y

# Using the lambda function
result = add(3, 5)
print(result)  # Output: 8

# Equivalent normal function to add two numbers
def add(x, y):
    return x + y

# Using the normal function
result = add(3, 5)
print(result)  # Output: 8


# List of numbers
numbers = [1, 2, 3, 4, 5]

# Lambda function to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
