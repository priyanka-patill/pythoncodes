class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"Car: {self.year} {self.make} {self.model}"

# Creating an object of the Car class
car1 = Car("Toyota", "Camry", 2020)

# Calling methods
print(car1.display_info())  # Output: Car: 2020 Toyota Camry
