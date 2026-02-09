import pytest
from sources.shapes import Rectangle


@pytest.fixture

def my_rectangle():
    return Rectangle(10,5)

@pytest.fixture

def weird_rectangle():
    return Rectangle(5,6)