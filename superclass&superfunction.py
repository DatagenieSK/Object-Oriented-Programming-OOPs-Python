#super() = function used in child class to call methods from parent class (superClass)
#          allows you to extent the functionality of the inheriantance methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):  # Inherit from Shape
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)  # Call superclass constructor
        self.radius = radius

    def describe(self):
        print(f"The area of circle is {3.14 * self.radius ** 2} cm^2")
        #now lets just call the describe function of the paresnt/ superclass
        super().describe()
class Sq(Shape):  # Inherit from Shape
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"The area of Square is {self.width ** 2} cm^2")
        # now lets just call the describe function of the paresnt/ superclass
        super().describe()
class Triangle(Shape):  # Inherit from Shape
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

# Create an instance of Circle
circle = Circle("red", True, 5)
sq = Sq('blue', False, 6)
triangle = Triangle("yellow", True, 10, 8)

print(circle.color)
print(f"the widh of the square is {sq.width}cm")
print(triangle.color)
print(triangle.is_filled)

circle.describe()
sq.describe()