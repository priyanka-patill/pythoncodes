# Define the Car class
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

# Create instances of the Car class
car1 = Car("Toyota", "Corolla", 2020, "Red")
car2 = Car("Honda", "Civic", 2019, "Blue")

# Accessing the attributes of the instances
print(f"Car 1: Make: {car1.make}, Model: {car1.model}, Year: {car1.year}, Color: {car1.color}")
print(f"Car 2: Make: {car2.make}, Model: {car2.model}, Year: {car2.year}, Color: {car2.color}")
