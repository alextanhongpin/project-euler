# < 100
# 41 = 2+3+5+7+11+13

# <1000
# 953 = ....21 terms

# <1000000

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


d = [] # d holds the consecutive sums
primes = []
i = 1
while i < 1000000:
    if is_prime(i):
        # 1. Get the prime numbers from 1 to n
        primes.append(i)
        # 2. Get the consecutive primes
        if len(d) - 1 >= 0:
            d.append(i + d[-1])
        else:
            d.append(i)
    i += 1

def get_closest(n, l):
    """
    n is the closest value
    l is the list
    """
    for i in range(len(l)):
        if l[i] >= n:
            return i
    return 0

num_combinations = 0
v = 0
for i in range(len(primes) - 1, 1, -1):
    prime = primes[i]
    try:
        n = d.index(prime) + 1
        if n > num_combinations:
            num_combinations = n
            v = prime
    except ValueError:
        n = get_closest(prime, d)
        start = d[n]
        for j in range(n + 1):
            if start - d[j] == prime:
                index = n - j
                if index > num_combinations:
                    num_combinations = index
                    v = prime

print "The prime {0} has {1} combinations".format(v, num_combinations)



