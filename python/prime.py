"""
Utility to check if a number is a valid prime number
"""

import math

def is_prime(number):
    """Check if a function is a prime number"""
    if number < 2:
        return False
    if number == 2 or number == 3:
        return True
    square_root = int(math.ceil(math.sqrt(number)))
    # We only reduce it down to 4, because 2 and 3 is a prime number
    for i in range(square_root + 1, 4, -1):
        if number % i == 0:
            return False
        elif number % 2 == 0:
            return False
        elif number % 3 == 0:
            return False
    return True
