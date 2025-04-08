class Animal:

    # attribute and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)

# create an object of the subclass
obj = Dog()

# access superclass attribute and method 
obj.name = "Rohu"
obj.eat()

# call subclass method 
obj.display()
