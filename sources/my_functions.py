def first_function(one_number,two_number):
    return one_number + two_number

def second_function(one_number,two_number):
    if two_number == 0:
        raise ValueError
    return one_number/two_number

def mul(one_number,two_number):
    if one_number == 0 or two_number == 0:
        raise ValueError
    return one_number * two_number

