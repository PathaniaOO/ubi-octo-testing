import math
from abc import ABC, abstractmethod


class Shape2D(ABC):
    """
    Abstract base class for all 2D shapes.

    This class defines a common interface that all 2D shapes
    (Circle, Rectangle, Square, etc.) must implement.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.

        Must be implemented by all subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.

        Must be implemented by all subclasses.
        """
        pass


class Circle(Shape2D):
    """
    Represents a circle defined by its radius.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with a given radius.

        :param radius: Radius of the circle (must be positive)
        :raises ValueError: If radius is zero or negative
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Formula: π * r²
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Formula: 2 * π * r
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape2D):
    """
    Represents a rectangle defined by length and breadth.
    """

    def __init__(self, length, breadth):
        """
        Initialize a Rectangle with length and breadth.

        :param length: Length of the rectangle (must be positive)
        :param breadth: Breadth of the rectangle (must be positive)
        :raises ValueError: If length or breadth is zero or negative
        """
        if length <= 0 or breadth <= 0:
            raise ValueError("Length and Breadth must be positive")
        self.length = length
        self.breadth = breadth

    def __eq__(self, other):
        """
        Compare two Rectangle objects for equality.

        Two rectangles are equal if both their length and breadth match.
        If 'other' is not a Rectangle (or subclass), comparison is not supported.
        """
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.length == other.length and self.breadth == other.breadth

    def area(self):
        """
        Calculate the area of the rectangle.

        Formula: length * breadth
        """
        return self.length * self.breadth

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Formula: 2 * (length + breadth)
        """
        return 2 * (self.length + self.breadth)


class Square(Shape2D):
    """
    Represents a square defined by the length of one side.
    """

    def __init__(self, side):
        """
        Initialize a Square with a given side length.

        :param side: Length of each side of the square
        """
        self.side = side

    def area(self):
        """
        Calculate the area of the square.

        Formula: side²
        """
        return self.side ** 2

    def perimeter(self):
        """
        Calculate the perimeter of the square.

        Formula: 4 * side
        """
        return 4 * self.side
