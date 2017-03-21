"""
Factorial digit sum
Problem 20
n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def factorial(n):
  return reduce(lambda x, y: x * y, [x for x in range(n, 1, -1)])



stringified = str(factorial(100))
print reduce(lambda x, y: x + y, [int(stringified[s]) for s in range(len(stringified))])