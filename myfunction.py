def greet():
    print('Hello World!')

# call the function
greet()
#---------------------------------------------------------
def greet(name):
    print("Hello", name)

# pass argument
greet("John")

#--------------------------------------------------------

# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:', square)
#---------------------------------------------------

# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4)

#---------------------------------------------------------
import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is",power)
#--------------------------------------------------
# function to sum any number of arguments
def add_all(*numbers):
    return sum(numbers)

# pass any number of arguments
print(add_all(1, 2, 3, 4))

#--------------------------------------------------------
# function to print keyword arguments
def greet(**words):
    for key, value in words.items():
        print(f"{key}: {value}")

# pass any number of keyword arguments
greet(name="John", greeting="Hello")

#Python Lambda Function Declaration
#lambda argument(s) : expression
#argument(s) - any value passed to the lambda function
#expression - expression is executed and returned
#---------------------------------------------------------------
# declare a lambda function
greet = lambda : print('Hello World')

# call lambda function
greet()

# Output: Hello World

#In Python, we can use the next() function to return the next item in the sequence.

# define a list
my_list = [4, 7, 0]

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))  # prints 4

# get the second element of the iterator
print(next(iterator))  # prints 7

# get the third element of the iterator
print(next(iterator))  # prints 0






