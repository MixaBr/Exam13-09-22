import math
from abc import ABC, abstractmethod


class Figures(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Figures):

    def __init__(self, side_length):
        self.side_length = side_length


    def area(self):
        return round(math.pow(self.side_length, 2), 2)

class Rectangle(Figures):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return round(self.a * self.b, 2)

class Circle(Figures):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * math.pow(self.radius, 2), 2)

square = Square(4)
rectangle = Rectangle(2,6)
circle = Circle(3)

figures = {square:"квадрата", rectangle:"прямоугольника", circle:"круга"}

for i, n in figures.items():
    print(f"Площадь {n} = {i.area()}")
