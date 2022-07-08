# Author: Xavier Rodriguez
# Date: 
# Description: test functions

import sierpinski
import math

def check_equal(fn_name, expected, result):
    """ Print the outcome of a test. Prints either PASS or FAIL, based
        on whether expected == result, followed by fn_name (the name
        of the function being tested), followed by expected and result
        values. """
    if expected == result:
        outcome = "PASS"
    else:
        outcome = "FAIL"
        
    print(outcome, fn_name, expected, result)

def test_midpoint():
    """ Tests the midpoint function """
    result = sierpinski.midpoint((0, 0), (2, 2))
    expected = (1.0, 1.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((4, 4), (0, 0))
    expected = (2.0, 2.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((0, 4), (0, 0))
    expected = (0.0, 2.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((4, 0), (0, 0))
    expected = (2.0, 0.0)
    check_equal("midpoint", expected, result)

#the new function
def test_distance():
    """this is used to find the distnace between the two points which also helps with
        finding the color in the trinalges"""
    result = sierpinski.distance(2,3,1,4)
    expected = (3)
    check_equal("distance", expected, result)
    
    result = sierpinski.distance(1,1,1,1)
    expected = (0)
    check_equal("distance", expected, result)
    
    result = sierpinski.distance(4,4,4,4)
    expected = (0)
    check_equal("distance", expected, result)
    
    result = sierpinski.distance(10,15,20,25)
    expected = (5)
    check_equal("distance", expected, result)

# write your function here to test one of your functions
# from sierpinski.py
    
if __name__ == "__main__":
    
     #test_midpoint()
     test_distance()
    
    # put a call to your test function here