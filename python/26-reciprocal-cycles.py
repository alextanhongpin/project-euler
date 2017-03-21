"""
Reciprocal cycles
Problem 26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from __future__ import division

def is_unique (n):
    counter = {}
    for i in range(len(n)):
        count = counter.get(n[i], 0)
        counter[n[i]] = count + 1
        if counter[n[i]] > 1:
            return False
    return True

def is_same(n):
    for i in range(len(n)):
        if n[0] != n[i]:
            return False
    return True

def is_half_same(a, b):
    return a == b

def get_repeating (n):
    print n
    out = str(n).split(".")[1]
    half = int(len(out) / 2)
    if is_unique(out):
        return out
    elif is_same(out):
        return out[0]
    elif is_half_same(out[:half], out[half:]):
        return out[:half]
    else:
        return out

max = -9999
max_int = 0
for i in range(1000):
    try:
        length = len(get_repeating(1 / i))
        if length > max:
            max = length
            max_int = i
    except ZeroDivisionError:
        print ''
print max_int, max

print get_repeating(1 / 2)
print get_repeating(1 / 3)
print get_repeating(1 / 4)
print get_repeating(1 / 5)
print get_repeating(1 / 6)
print get_repeating(1 / 7)
print get_repeating(1 / 8)
print get_repeating(1 / 9)
print get_repeating(1 / 10)