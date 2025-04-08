from scipy import linalg 
import numpy as np 
  
# The function takes two arrays 
a = np.array([[6, 2], [5, 5]]) 
b = np.array([8, 10]) 
  
# Solving the linear equations 
res = linalg.solve(a, b) 
print(res)
"""
6x + 2y = 8
5x + 5y = 10
"""
