import math
n = 1100


from prime import is_prime
def circular_number(n):
  arr = []
  str_n = str(n)
  for i in range(len(str(n))):
    first = str_n[0]
    str_n = str_n.replace(first, "", 1)
    str_n += first
    arr.append(int(str_n))
  return arr


def circular_primes(n):
  c = circular_number(n)
  p = list(filter(lambda x: is_prime(x), c))
  return len(c) == len(p)

def main():
    """The main application"""
    count = 0
    for i in range(1, 1000000):
      if i % 2 != 0 or i is 2:
        if circular_primes(i) == True:
          count += 1
    print count

if __name__ == '__main__':
    import timeit
    ITERATIONS = 10
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
