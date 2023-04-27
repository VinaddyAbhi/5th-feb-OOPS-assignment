#!/usr/bin/env python
# coding: utf-8

#  Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.
#   
#   
#   Soltion:
#   
#   
# A class is defined using the "class" keyword, followed by the name of the class, and a colon. The body of the class contains the 
# properties and methods of the class. An object is created by calling the class as if it were a function, which returns a new instance of the class.

# In[3]:


class Car:
    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def start(self):
        print("Starting the car.")

    def accelerate(self):
        print("Accelerating the car.")

    def brake(self):
        print("Applying the brakes.")

    def turn(self, direction):
        print("Turning the car to the", direction)

my_car = Car("Honda", "Civic", "Blue", 2023, 5000)


# In[4]:


print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.year)
print(my_car.mileage)


# Q2. Name the four pillars of OOPs.
# 
# Solution:
# 
# The four pillars of Object-Oriented Programming (OOP) are:
# 
# Encapsulation: It is a mechanism that restricts access to the properties and methods of an object to only the relevant code. It helps in achieving data hiding and abstraction.
# 
# Inheritance: It is a mechanism by which a class can derive the properties and methods of another class. The derived class (also called subclass) can inherit the properties and methods of the base class (also called superclass) and can also add its own properties and methods.
# 
# Polymorphism: It is the ability of an object to take on multiple forms. It allows a single object to be treated as if it belongs to multiple types. Polymorphism is achieved through method overloading and method overriding.
# 
# Abstraction: It is the process of hiding the complexity of a system and exposing only the essential features to the user. In OOP, abstraction is achieved through abstract classes and interfaces. It helps in achieving modularity, maintainability, and flexibility of code.
# 

# Q3. Explain why the __init__() function is used. Give a suitable example.
# 
# Solution:
# 
# The init() function is a special method in Python classes that is used to initialize the object's properties when it is created. It is also known as the constructor method. The name of the method starts and ends with double underscores.
# 
# The init() method is called automatically when an object is created, and it is used to set the initial state of the object's properties. This method can also accept arguments that are used to initialize the object's properties.
# 
# 

# In[6]:


#Example

class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)

student1 = Student("John", 18, "S001")
student1.display_details()


# Q.4 Why self is used in OOPs?
# 
# Solution:
# 
# In Python's Object-Oriented Programming (OOP), the "self" keyword is used to refer to the instance of the class that is being manipulated. It is a reference to the object that the method is being called on. The self keyword is used to pass the object as an argument to the class method.
# 
# When we create an object of a class, we can access its properties and methods using the dot (.) notation. The self keyword is used to specify which object's properties and methods we want to access or modify. It helps to differentiate between the properties and methods of different objects of the same class.

# Q.5 What is inheritance? Give an example for each type of inheritance.
# 
# Solution:
# 
# Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a new class to be based on an existing class. The new class inherits the properties and behaviors of the existing class and can also add its own properties and behaviors. Inheritance provides a way to reuse code, reduce duplication, and increase code flexibility and maintainability.
# 
# There are four types of inheritance:
# 
# Single inheritance: In single inheritance, a subclass inherits properties and methods from a single superclass. The subclass can also add its own properties and methods. Here's an example:

# In[8]:


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("I am an animal.")

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def speak(self):
        print("Woof!")

my_dog = Dog("Fido", "Canis lupus familiaris", "Labrador Retriever")
print(my_dog.name)
print(my_dog.species)
print(my_dog.breed)
my_dog.speak()


# Multiple inheritance: In multiple inheritance, a subclass inherits properties and methods from multiple superclasses. The subclass can also add its own properties and methods. Here's an example:

# In[10]:


class Animal:
    def speak(self):
        print("I am an animal.")

class Mammal:
    def feed_young(self):
        print("I am feeding my young.")

class Dog(Animal, Mammal):
    def speak(self):
        print("Woof!")

my_dog = Dog()
my_dog.speak()
my_dog.feed_young()


# Multi-level inheritance: In multi-level inheritance, a subclass inherits properties and methods from a superclass, which in turn inherits from another superclass. Here's an example:

# In[11]:


class Animal:
    def speak(self):
        print("I am an animal.")

class Mammal(Animal):
    def feed_young(self):
        print("I am feeding my young.")

class Dog(Mammal):
    def speak(self):
        print("Woof!")

my_dog = Dog()
my_dog.speak()
my_dog.feed_young()


# Hierarchical inheritance: In hierarchical inheritance, multiple subclasses inherit from a single superclass. Here's an example:

# In[12]:


class Animal:
    def speak(self):
        print("I am an animal.")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

my_dog = Dog()
my_dog.speak

