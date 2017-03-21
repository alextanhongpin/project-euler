"""Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math
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

prime = 2
count = 0
total = 0
max = 2000000
while prime < max:
  if is_prime(count):
    prime = count
    if (prime < max):
      total += prime
      print("Prime found:", prime)
    else:
      break
  count += 1

print("The total of prime below 2 million is:", total)