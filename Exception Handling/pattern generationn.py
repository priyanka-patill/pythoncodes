import re

# Function to validate the password
def validate_password(password):
    # Regular expression pattern for the password validation
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$'

    # Using re.match() to check if the password matches the pattern
    if re.match(pattern, password):
        return True
    else:
        return False

# Prompt user to enter a password
password = input("Enter a password: ")

# Validate the entered password
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. Make sure it meets the following criteria:")
    print("1. At least 8 characters long")
    print("2. Contains at least one uppercase letter")
    print("3. Contains at least one lowercase letter")
    print("4. Contains at least one digit")
    print("5. Contains at least one special character (!@#$%^&*)")
