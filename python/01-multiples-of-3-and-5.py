"""
Problem 1: Get the sum of all multiples from
"""

from benchmark import Benchmark
import timeit

def main():
    """
    The main application
    """
    output = set()
    for i in range(1000):
        if i % 3 == 0:
            output.add(i)
        if i % 5 == 0:
            output.add(i)
    return sum(output)

with Benchmark() as t:
    main()
print  "=> %s s" % t.secs
