import pytest
from sources.shapes import Circle,Rectangle
import math

class TestCircle:
    
    def setup_method(self,method):
        print(f"setting up {method}")
        self.circle = Circle(10)
        
        
    def teardown_method(self,method):
        print(f"setting up {method}")
        del self.circle
    
    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
    
    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius
    
    def test_not_same(self,my_rectangle):
        assert self.circle.area() != my_rectangle.area()
        
    
class TestRectangle:  
    def test_rectangle_area(self):
        r = Rectangle(5,10)
        assert r.area() == 50
    
    def test_rectangle_perimeter(self):
        r = Rectangle(5,10)
        assert r.perimeter() == 30
        

    @pytest.mark.parametrize("length,breadth",[
        (-5,10),
        (5,-10)
    ])
    def test_rectangle_invalid(self,length,breadth):
        with pytest.raises(ValueError):
            Rectangle(length,breadth)
            
        