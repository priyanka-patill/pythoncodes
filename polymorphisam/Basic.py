"""
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

Create a Class
To create a class, use the keyword class:
"""

class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

"""
All classes have a function called __init__(), which is always executed
when the class is being initiated.

Use the __init__() function to assign values to object properties,
or other operations that are necessary to do when the object is being created:
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("amit", 36)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    #print("Hello my name is " + self.name + "and my age is " + self.age)
     print("Hello my name is " + self.name + " and my age is " + str(self.age))
     print(f"Hello my name is {self.name} and my age is {self.age}")



p1 = Person("vansh", 18)
p1.myfunc()






