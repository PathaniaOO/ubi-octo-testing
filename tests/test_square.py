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

 
# FOR DIFFERENT VALUES BETTER then FOR LOOP
@pytest.mark.parametrize("side,expected_area",[(5,25), (4,16)])
def test_multiple_square_areas(side,expected_area):
    assert Square(side).area() == expected_area


@pytest.mark.parametrize("side,expected_perimeter", [(2,8), (3,12)])
def test_multiple_square_perimeter(side,expected_perimeter):
    assert Square(side).perimeter() == expected_perimeter
