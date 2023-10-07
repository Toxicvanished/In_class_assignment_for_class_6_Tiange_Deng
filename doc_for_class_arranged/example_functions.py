# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen 
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html
from typing import Union

def my_adder(a: Union[float, int], b: Union[float, int], c: Union[float, int]) -> Union[float, int]:
    """
    Function to sum the 3 numbers;
    Input: 3 numbers a, b, c, int or float;
    Output: the sum of a, b, and c, int or float.
    """
    
    # this is the summation
    out = a + b + c
    
    return out


def my_thermo_stat(temp:int , desired_temp:int) -> str:
    """
    Changes the status of the thermostat based on temperature and desired temperature.
    Input 1: Current temperature, int;
    Input 2: Desired temperature, int;
    Output: 'Heat' for heating up, 'AC' for cooling down, 'off' for keepig cunrrent temperature.
    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status

 
def have_digits(s: str) -> int:
    """
    Check if a string has digits in it.
    Input: a random string;
    Output: int, 0 for no digit detected, 1 for digit detected.
    """
    
    out = 0
    
    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break
            
    return out
    
 
