"""
Lexicographic permutations

Problem 24

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the
digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

# Use permutations to solve the equation
from __future__ import division
from timeit import default_timer as timer
import math

start_time = timer()

initial = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

def combinations(data):
    """
      return the possible combinations
    """
    return math.factorial(data)




c = combinations(len(initial))
c_count = c / len(initial)
print "The number of possible combinations are", c
print "For each section (0-3), they will have", c_count, "combinations"
# print "For the millionth position, it has to be at:", input[1000000 / (combinations(10, 1) // 10)]

length = len(initial)

def nth_index(arr, i):
    """
      get
    """
    step = combinations(len(arr)) / len(arr)
    out = int(math.floor(i / step)) - 1 if i % step == 0 else int(math.floor(i / step))

    return out % len(arr)
def remainder(arr, i):
    step = combinations(len(arr)) / len(arr)
    return i if i % step == 0 else math.floor(i / step) * step
    # return i if i % step == 0 else i % step
output = []
nth = 1000000
first_index = nth_index(initial, nth)

first_value = list(initial)[first_index]
initial.remove(first_value)
output.append(first_value)

loop = 0
while len(output) < length:
  loop += 1
  step = combinations(len(initial)) / len(initial)
  next_index = nth_index(initial, nth)
  nth -= remainder(initial, nth)
  next_value = list(initial)[next_index]
  initial.remove(next_value)
  output.append(next_value)

print "".join(map(lambda x : str(x), output))

end_time = timer()
print "Time:", end_time - start_time