import math
import pytest
from sources.shapes import Circle, Rectangle


class TestCircle:
    """
    Test suite for the Circle class.

    Each test gets a fresh Circle instance created in setup_method
    and destroyed in teardown_method to avoid shared state.
    """

    def setup_method(self, method):
        """
        Runs before every test method in this class.

        Creates a Circle instance with radius 10 that can be reused
        by all test methods via self.circle.
        """
        print(f"setting up {method}")
        self.circle = Circle(10)

    def teardown_method(self, method):
        """
        Runs after every test method in this class.

        Cleans up the Circle instance to ensure no state leaks
        between tests.
        """
        print(f"tearing down {method}")
        del self.circle

    def test_area(self):
        """
        Verify that the area of the circle is calculated correctly.

        Formula: π * r²
        """
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        """
        Verify that the perimeter (circumference) of the circle
        is calculated correctly.

        Formula: 2 * π * r
        """
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius

    def test_not_same(self, my_rectangle):
        """
        Ensure that the area of a Circle is not equal to the area
        of a Rectangle fixture.

        This test checks logical inequality between different shapes.
        """
        assert self.circle.area() != my_rectangle.area()


class TestRectangle:
    """
    Test suite for the Rectangle class.
    """

    def test_rectangle_area(self):
        """
        Verify that the rectangle area is calculated correctly.

        Formula: length * breadth
        """
        r = Rectangle(5, 10)
        assert r.area() == 50

    def test_rectangle_perimeter(self):
        """
        Verify that the rectangle perimeter is calculated correctly.

        Formula: 2 * (length + breadth)
        """
        r = Rectangle(5, 10)
        assert r.perimeter() == 30

    @pytest.mark.parametrize("length,breadth", [
        (-5, 10),
        (5, -10),
    ])
    def test_rectangle_invalid(self, length, breadth):
        """
        Verify that Rectangle raises a ValueError when initialized
        with invalid (non-positive) dimensions.

        This test runs multiple times using different invalid inputs.
        """
        with pytest.raises(ValueError):
            Rectangle(length, breadth)
