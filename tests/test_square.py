import pytest
from sources.shapes import Square

@pytest.fixture

def square():
    return Square(10)
    
def test_area(square):
    assert square.area() == 10 ** 2

def test_perimeter(square):
    assert square.perimeter() == 4*10
    
