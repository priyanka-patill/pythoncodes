# Empty dictionary
my_dict = {}

# Dictionary with initial key-value pairs
my_dict = {
    "Name": "Alice",
    "Age": 25,
    "City": "Mumbai"
}

print(my_dict)
print("---------------------------------------------------------------")

#1.The get() method returns the value of the item with the specified key.

age = my_dict.get("Age")
print(age)

print("---------------------------------------------------------------")

#2.dict.keys(): Returns a new view object that displays a list of all the keys in the dictionary.
keys = my_dict.keys()
print(keys)  
print("---------------------------------------------------------------")

#3.dict.values(): Returns a new view object that displays a list of all the values in the dictionary.
values = my_dict.values()
print(values)

print("---------------------------------------------------------------")

#4.dict.items(): Returns a new view object that displays a list of dictionary's key-value tuple pairs.
items = my_dict.items()
print(items)
print("---------------------------------------------------------------")
#5.dict.update([other]): Updates the dictionary with the key-value pairs from another dictionary
#or iterable of key-value pairs.If the key is already present, its value is updated.
my_dict.update({"Country": "India"})
print(my_dict)
print("---------------------------------------------------------------")
#6.dict.pop(key): Removes the specified key and returns the corresponding value.
#If the key is not found, the default value is returned if provided; otherwise, it raises a KeyError.
my_dict.pop("Age")
print(my_dict)
print("---------------------------------------------------------------")
#7.dict.clear(): Removes all items from the dictionary.
my_dict.clear()
print(my_dict)
print("---------------------------------------------------------------")
original_dict = {
    "Name": "Alice",
    "Age": 25,
    "City": "Mumbai"
}

# 8.copy():Returns a copy of the dictionary
copied_dict = original_dict.copy()
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)
print("---------------------------------------------------------------")
#The popitem() method in Python's dictionary is used to remove and return a key-value pair from the dictionary. This method removes the last inserted key-value pair
my_dict = {
    "Name": "Alice",
    "Age": 25,
    "City": "Mumbai"
}

# Removing and returning the last inserted key-value pair
last_item = my_dict.popitem()

print("Removed Item:", last_item)
print("Updated Dictionary:", my_dict)

