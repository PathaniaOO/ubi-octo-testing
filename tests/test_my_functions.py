import pytest,time
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

#MARK
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = second_function(10,5)
    assert result == 2


@pytest.mark.skip(reason = "This feature is currently broken")#skip a test
def test_add():
    assert first_function(1,3) == 4
    
    
@pytest.mark.xfail(reason = "We know we cant divide by zero")
def test_divide_zero_broken():
    second_function(20,0)