# Prompt the user to enter a number
number = int(input("Enter a number to generate its multiplication table: "))

# Generate and display the multiplication table
print(f"\nMultiplication table for {number}:\n")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
