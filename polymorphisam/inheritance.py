"""
Python Inheritance
Inheritance allows us to define a class that inherits all
the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called
derived class.
"""
# Parent or Base Class
class Calculate:
    def sum(self, a, b):
        print(a + b)
 
# Subclass or Derived Class
class Number(Calculate):
    pass
 
obj = Number()
obj.sum(8, 90)
 
#---------class has constuctor
# Base class
class Hero:
    # Constructor function
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
 
    def show(self):
        print(self.name)
        print(self.surname)
 
# Derived class
class Name(Hero):
    def __init__(self, initial, name, surname):
        self.initial = initial
        # Calling the __init__ of the parent class
        Hero.__init__(self, name, surname)
 
    def display(self):
        print(self.initial)
        Hero.show(self)
 
obj = Name("ABK", "Arun", "Kulkarni")
obj.display()
print("-"*20)
obj.show()
#---------------------------multilevel

# Base Class
class GrandPa:
    def __init__(self):
        self.age = 100
 
# Derived CLass
class Parent(GrandPa):
    def __init__(self):
        self.name = "Geek"
        GrandPa.__init__(self)
 
# Derived Class
class GrandChild(Parent):
    def __init__(self):
        self.hobby = "Gaming"
        Parent.__init__(self)
 
    def display(self):
        print("Grandpa:", self.age)
        print("Parent:", self.name)
        print("Grandchild:", self.hobby)
 
obj = GrandChild()
obj.display()
#-------------------------------------Hierarchical Inheritance
# Base Class
class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def division(self):
        print(self.a / self.b)
 
# Derived Class
class Add(Calculate):
    def __init__(self, a, b):
        Calculate.__init__(self, a, b)
 
    def add(self):
        print("Addition:", self.a + self.b)
        Add.division(self)
 
# Derived Class
class Subtract(Calculate):
    def __init__(self, a, b):
        Calculate.__init__(self, a, b)
 
    def subtract(self):
        print("Subtraction:", self.a - self.b)
        Subtract.division(self)
 
obj1 = Add(34, 98)
obj2 = Subtract(45, 67)
obj1.add()
obj2.subtract()
#------------------------------------hybrid inheritance.

# Base Class
class Role:
    def role(self):
        print("Protagonist")
 
# Derived Class
class Luffy(Role):
    def power(self):
        print("Gum-Gum devil fruit")
 
# Derived Class
class Naruto(Role):
    def power1(self):
        print("Nine-tail fox")
 
# Derived Class
class Anime(Luffy, Naruto):
    def anime(self):
        print("They are anime characters.")
 
obj = Anime()
obj.role()
obj.power()
print("-"*20)
obj.role()
obj.power1()
print("-"*20)
obj.anime()















