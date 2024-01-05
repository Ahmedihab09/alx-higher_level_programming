#!/usr/bin/python3

'''Rectangle class'''


class Rectangle:
    """A class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
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
        """Set the height of the Rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if either the width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable string representation of the Rectangle.

        The rectangle is represented by the `print_symbol` multiplied by the width and height.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol_str = str(self.print_symbol)
        line = symbol_str * self.__width
        return "\n".join([line for _ in range(self.__height)])

    def __repr__(self):
        """Return the string representation of the Rectangle instance.

        This string is a valid Python expression that can recreate the instance.

        Returns:
            str: The Python expression to recreate the instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message and decrement the number_of_instances when a Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on the area, or rect_1 if equal.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If either of rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The rectangle with the greater area, or rect_1 if they are equal.
        """
        if not isinstance(rect_1, Rectangle) or not isinstance(rect_2, Rectangle):
            raise TypeError(f"{'rect_1' if not isinstance(rect_1, Rectangle) else 'rect_2'} must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

