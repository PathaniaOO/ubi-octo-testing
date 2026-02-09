import math
from abc import ABC,abstractmethod
class Shape2D:
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape2D):
        
        def __init__(self,radius):
            if radius <= 0:
                raise ValueError("Radius must be positive")
            self.radius = radius
        
        def area(self):
             return  math.pi * self.radius ** 2
         
        def perimeter(self):
             return  2 * math.pi * self.radius
         
class Rectangle(Shape2D):
    def __init__(self,length,breadth):
        if length <= 0  or breadth <= 0:
            raise ValueError ("Length and Breadth must be positive")
        self.length = length
        self.breadth = breadth 
        
    def __eq__(self, other):
        if not isinstance(other,Rectangle):
            return NotImplemented
        return self.breadth == other.breadth and self.length == other.length 
    
    def area(self):
         return self.length * self.breadth
    
    def perimeter(self):
         return 2*(self.length+self.breadth)

class Square(Shape2D):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
         return 4 * self.side


         
        