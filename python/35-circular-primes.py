import math
n = 1100


def circular_number(n):
  arr = []
  str_n = str(n)
  for i in range(len(str(n))):
    first = str_n[0]
    str_n = str_n.replace(first, "", 1)
    str_n += first
    arr.append(int(str_n))
  return arr

def is_prime (n):
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

def circular_primes(n):
  c = circular_number(n)
  p = list(filter(lambda x: is_prime(x), c))
  return len(c) == len(p)

count = 0
for i in range(1, 1000000):
  if i % 2 != 0 or i is 2:
    print i
    if circular_primes(i) == True:
      print "PRIME", i
      count += 1
print count