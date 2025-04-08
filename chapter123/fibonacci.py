x = [("Alice", 85), ("Bob", 90), ("Charlie", 78), ("Diana", 92)]
y = dict(x)
print(y)  # Output: {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'Diana': 92}
y={k:v for k,v in x}
print(y)  

