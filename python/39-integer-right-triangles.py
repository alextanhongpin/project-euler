
import math


# a ** 2 + b ** 2 = c ** 2
# a + b + c = p
# b = (p ** 2 - 2 * p * a) / (2 * p - 2 * a)

def is_solution (a, p):
    n = (p ** 2 - 2 * p * a)
    d = (2 * p - 2 * a)
    if d is 0:
      return False
    return n % d == 0


def main():
    """
    Start Program here
    """
    output = 0
    n = 0
    for p in range(1000, 0, -1):
      count = 0
      for a in range(1000, 1, -1):
        if is_solution(a, p):
          count += 1
      if count > output:
        output = count
        n = p

    print "Answer:", output, n

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
