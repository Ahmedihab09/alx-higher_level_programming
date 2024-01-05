#!/usr/bin/python3

'''Rectangle class'''


class Rectangle:
    """A class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable string representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol_str = str(self.print_symbol)
        line = symbol_str * self.__width
        return "\n".join([line for _ in range(self.__height)])

    def __repr__(self):
        """Return the string representation of the Rectangle instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message and decrement the number_of_instances when a Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on the area."""
        if not isinstance(rect_1, Rectangle) or not isinstance(rect_2, Rectangle):
            raise TypeError(f"{'rect_1' if not isinstance(rect_1, Rectangle) else 'rect_2'} must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)
