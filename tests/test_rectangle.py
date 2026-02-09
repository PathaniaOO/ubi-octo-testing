import pytest
from sources.shapes import Rectangle

#MADE A CONFEST FILE FOR THE FIXTURES 

def test_area(my_rectangle):
    """
    Verify that the area of a rectangle is calculated correctly.

    Uses the `my_rectangle` fixture, which is expected to return
    a Rectangle instance with length 10 and breadth 5.
    """
    assert my_rectangle.area() == 10 * 5


def test_perimeter(my_rectangle):
    """
    Verify that the perimeter of a rectangle is calculated correctly.

    Formula: 2 * (length + breadth)
    """
    assert my_rectangle.perimeter() == 2 * (10 + 5)


def test_not_equal(my_rectangle, weird_rectangle):
    """
    Verify that a Rectangle is not considered equal to an object
    of a different type.

    This test relies on Rectangle.__eq__ returning NotImplemented
    for unsupported comparisons.
    """
    assert my_rectangle != weird_rectangle
