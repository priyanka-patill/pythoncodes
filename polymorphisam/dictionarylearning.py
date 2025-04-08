"""
my_dict = {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}

def get_value_by_index(dictionary, index):
    
    key = list(dictionary.keys())[index]
    print(key)
    return dictionary[key]

# Example usage
index = 1
value = get_value_by_index(my_dict, index)
print(f"Value at index {index}: {value}")  # Output: 25
"""
A={"Rice":51, "sunflower oil": 150, "choclate":100}
print(A)
fa=[]
f=[1,2,0]
for i in f:
    key = list(A.keys())[i]
    #print(key)
    value=A[key]
    print(value)
    fa.append(value)
print(fa)
  
    

