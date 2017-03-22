import math
import re

def is_prime(n):
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

main()