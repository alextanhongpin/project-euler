import math
import re

from prime import is_prime

def truncate_left(n):
  arr = [n]
  out = str(n)
  for i in range(1, len(str(n))):
    first = out[0]
    out = out.replace(first, "", 1)
    arr.append(int(out))
  return arr

def truncate_right(n):
  arr = [n]
  out = str(n)
  for i in range(1, len(str(n))):
    last = out[-1]
    out = re.sub(last + "$", "", out)
    arr.append(int(out))
  return arr

def list_is_prime(arr):
  if len(arr) < 2:
    return False
  prime_only = filter(lambda x: is_prime(x), arr)
  return len(prime_only) == len(arr)

def main():
  """The main application"""
  i = 1
  arr = []
  count = 0
  while count < 11:
    i += 2
    print i, count
    if list_is_prime(truncate_left(i)) and list_is_prime(truncate_right(i)):
      arr.append(i)
      count += 1

  print sum(arr), arr


if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
