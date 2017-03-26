"""
  # Coin sums

  Problem 31
  ----------
  In England the currency is made up of pound, E, and pence, p, and there are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, E1 (100p) and E2 (200p).
  It is possible to make E2 in the following way:

  1xE1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
  How many different ways can E2 be made using any number of coins?
"""

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
