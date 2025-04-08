import math

# Function to calculate the area of a circle
def area_circle(radius):
    return math.pi * radius ** 2

# Function to calculate the area of a rectangle
def area_rectangle(length, width):
    return length * width

# Function to calculate the area of a triangle
def area_triangle(base, height):
    return 0.5 * base * height

def main():
    while True:
        print("\nArea Calculator Menu:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            radius = float(input("Enter the radius of the circle: "))
            print(f"The area of the circle is: {area_circle(radius):.2f}")
        elif choice == '2':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print(f"The area of the rectangle is: {area_rectangle(length, width):.2f}")
        elif choice == '3':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print(f"The area of the triangle is: {area_triangle(base, height):.2f}")
        elif choice == '4':
            print("Exiting Area Calculator.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
