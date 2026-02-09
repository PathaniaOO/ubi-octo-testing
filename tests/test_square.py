import pytest
from sources.shapes import Square


@pytest.fixture
def square():
    """
    Pytest fixture that provides a Square instance.

    This fixture creates a Square with side length 10 and
    injects it into any test function that requests `square`
    as a parameter.
    """
    return Square(10)


def test_area(square):
    """
    Verify that the area of the square is calculated correctly.

    Formula: side²
    """
    assert square.area() == 10 ** 2


def test_perimeter(square):
    """
    Verify that the perimeter of the square is calculated correctly.

    Formula: 4 * side
    """
    assert square.perimeter() == 4 * 10
