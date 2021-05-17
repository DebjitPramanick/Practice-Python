from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0

# Shape class will oblige to all other inherited classes to have a function called printArea


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printArea(self):
        return self.length*self.breadth

class Circle(Shape):
    type = "Circle"

    def __init__(self):
        self.radius = 4

    def printArea(self):
        return 3.14*(self.radius**2)


rect1 = Rectangle()
circ1 = Circle()

print(rect1.printArea(), circ1.printArea())
