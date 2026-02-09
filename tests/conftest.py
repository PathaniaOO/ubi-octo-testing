import pytest
from sources.shapes import Rectangle

@pytest.fixture
def my_rectangle():
    """
    Fixture providing a valid Rectangle instance.
    """
    return Rectangle(10, 5)

@pytest.fixture
def weird_rectangle():
    """
    Fixture providing an object that is NOT a Rectangle.
    Used to test inequality behavior.
    """
    return "not a rectangle"
