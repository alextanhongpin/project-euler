# 1487, 4817, 8147
# step: 3330
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

def unique(n):
    a = [str(n)[i] for i in range(len(str(n)))]
    a.sort()
    return int("".join(a))

s = set()
n = 0
# First, get the primes with 4-digits
primes = filter(lambda x: x is not None, [ i if is_prime(i) else None 
                                           for i in range(1000, 9999)])

while len(s) < 3:
    print "N", n
    for i in range(len(primes)):
        a = n * 0 + primes[i]
        b = n * 1 + primes[i]
        c = n * 2 + primes[i]
        if a in primes and b in primes and c in primes:
            if a != b and b != c:
                if unique(a) == unique(b) and unique(b) == unique(c):
                    s.add(a)
                    s.add(b)
                    s.add(c)
                    print a, b, c
    n += 1
