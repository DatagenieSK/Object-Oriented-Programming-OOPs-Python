'''
@property = Decorator used to define a method as a property (it can be accessed like an attribute)
            Benefit: adds additional logic when reading, writing, or deleting attributes.
            Provides getter, setter, and deleter methods.
'''

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, newwidth):
        if newwidth > 0:
            self._width = newwidth
        else:
            print("Width cannot be less than zero")

    @height.setter
    def height(self, newheight):
        if newheight > 0:
            self._height = newheight
        else:
            print("Height cannot be less than zero")  # Fixed error message

    @width.deleter
    def width(self):
        print("Width is deleted")
        del self._width

rectangle = Rectangle(3, 4)

rectangle.height = 5
rectangle.width = 10

print(rectangle.width)   # Output: 10.0cm
print(rectangle.height)  # Output: 5.0cm

del rectangle.width  # Deletes _width

# Handling missing attribute after deletion
try:
    print(rectangle.width)  # This will raise an AttributeError
except AttributeError:
    print("Width attribute has been deleted.")
