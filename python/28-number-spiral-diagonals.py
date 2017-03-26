"""
https://projecteuler.net/problem=28
Answer: 669171001
"""
from __future__ import division

def main():
    """The main application"""
    grid = 1001
    grid_size = grid * grid

    tt = 0
    for y in range(1, grid + 1, 2):
      for x in range(1, grid_size + 1, 2):
        if x == 1 and y == 1:
          tt += 1
        if x > (y - 2) * (y - 2) and x <= y * y:
          if ((y * y) - x) % (y - 1) == 0:
            tt += x
    print tt

if __name__ == '__main__':
    import timeit
    ITERATIONS = 5
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
