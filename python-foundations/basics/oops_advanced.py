"""
oops.py
Topic: Little Advanced OOP - Inheritance, Polymorphism, Encapsulation
"""

import math


# 1. Inheritance - Person and Student
class Person:
    def __init__(self, name):
        self.name = name

    def intro(self):
        return f"Hi, I'm {self.name}"


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def intro(self):  # overriding the parent method
        return f"{super().intro()} and I study {self.course}"


# 2. Polymorphism - Shapes
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)


if __name__ == "__main__":
    print("\n--- INHERITANCE ---")
    s = Student(input("Enter name: "), input("Enter course: "))
    print(s.intro())

    print("\n--- POLYMORPHISM ---")
    shapes = [Rectangle(float(input("Length: ")), float(input("Width: "))),
              Circle(float(input("Radius: ")))]
    for shape in shapes:
        print(type(shape).__name__, "area:", shape.area())