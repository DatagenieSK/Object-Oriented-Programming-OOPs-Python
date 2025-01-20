# polymorphism = greek word that means to have many faces and forms

# poly = many
# morphe = form
# two ways to achive Polymorphism
#1. inheriantance 2. duck typing= object must have necessary methods/attributes


#this is method 1. inheriantance
from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self,width):
        self.width = width

    def area(self):
        return self.width ** 2

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.topping = toppings

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("corn", 15)]


for shape in shapes:
    print(f"{shape.area()} cm²") #² is alt + 0178


#method 2 Duck typing
# object must have the minimum necessary attributes/methods
#"if it looks like a duck and Quack like a duck, it must be a duck"



class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Car:
    alive = False
    #def horn(self):
       # print("Honk")

    #lets chage this to speak to make it work
    def speak(self):
        print("Honk")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)