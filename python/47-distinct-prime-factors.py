"""
TODO: Optimize the solution
"""

import math

def is_prime (n):
  """
    Checks if a number is a prime number
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

def get_divisors(n):
  s = set()
  for i in range(n):
    try:
      if n % i == 0:
        s.add(i)
    except ZeroDivisionError:
      continue
  return list(s)

def is_prime_list(l):
  o = [i if is_prime(i) else None for i in l]
  return list(filter(lambda x: x is not None, o))


def main():
  primes = []
  i = 100
  max_count = 4
  found = False
  count = 0
  while found is False:
    i += 1
    l = get_divisors(i)
    if len(is_prime_list(l)) == max_count:
      print "FUD", i, count
      if len(primes) - 1 > 0:
        if i - primes[len(primes)-1] == 1:
          count += 1
          if count == max_count - 1:
            print "ANSWER", primes[-3]
            found = True
        else: 
          count = 0
      primes.append(i)



  arr = []
  for i in range(len(primes)):
    if i + 3 < len(primes):
      if primes[i + 1] - primes[i] == 1 and primes[i + 2] - primes[i] == 2 and primes[i + 3] - primes[i] == 3:
        arr.append([primes[i], primes[i + 1], primes[i + 2], primes[i + 3]])

  print len(arr), arr

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)


