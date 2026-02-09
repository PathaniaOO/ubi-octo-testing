import pytest
from sources.my_functions import first_function,second_function,mul

def test_add():
    result = first_function(1,5)
    assert result == 6

def test_add_strings():
    resut  = first_function("What The ","Hell")
    assert resut == 'What The Hell'

def test_divide():
    result = second_function(10,2)
    assert round(result,1) == 5
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
        second_function(10,0)

def test_mul():
    result = mul(10,2)
    assert result == 20

