"""
https://projecteuler.net/problem=27

Answer:
a = -61
b = 971
a x b = -59231
"""
import math

def is_prime(n):
  """
    Check if the number is a prime number or not
  """
  if n <= 1:
    return False
  elif n == 2:
    return True
  elif n == 3:
    return True
  else:
    square_root = int(math.ceil(math.sqrt(n)))
    for i in range(square_root + 1, 2, -1):
      if n % i == 0:
        return False
      elif n % 2 == 0:
        return False
      elif n % 3 == 0:
        return False
    return True

def quadratic_primes_function(a, b, x):
  """
    
  """
  return x ** 2 + a * x + b

def count_primes(a, b):
  counter = 0
  for x in range(80):
    if is_prime(quadratic_primes_function(a, b, x)):
      counter += 1
    else:
      return counter
  return counter


def main():
  final_a = 0
  final_b = 0
  final_count = -9999
  for a in range(-1000, 1000):
    for b in range(-1000, 1000):
      count = count_primes(a, b)
      if count > final_count:
        final_count = count
        final_a = a
        final_b = b
  print final_count, final_a * final_b


if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
