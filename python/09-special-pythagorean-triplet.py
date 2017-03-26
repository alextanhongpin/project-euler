"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math

def f (a, b, c):
    return a + b + c

def circle (a, b):
    return math.sqrt(a ** 2 + b ** 2)

def main():
    """The main application"""
    s = set()
    for a in range(1, 1001):
        for b in range(1, 1001):
            c = circle(a, b)
            if f(a, b, c) == 1000:
                s.add(a)
                s.add(b)
    c = circle(list(s)[0], list(s)[1])
    s.add(c)
    print("The product abc is:", reduce((lambda x, y: x * y), s))

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
