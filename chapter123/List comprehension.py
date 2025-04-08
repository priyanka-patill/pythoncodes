#List Comprehension
x=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(x)
#------------------------------------
squares = [x**2 for x in range(1, 11)]
print(squares)
#------------------------------------------------
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)
#---------------------------------------------------------------------
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)
#--------------------------------------------------------------------
even_squares_dict = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares_dict)

