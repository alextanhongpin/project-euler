"""
Problem 23: Non-abundant sums
"""

def is_abundant(n):
    """Check if a number is abundant"""
    arr = []
    for i in range(0, n):
      try:
        if n % i == 0:
          arr.append(i)
      except ZeroDivisionError:
          ""
    return sum(arr) > n

def main():
  """The main application"""
  n = 28123
  sum_abundants = []
  abundants = []
  for i in range(n + 1):
    if is_abundant(i):
      abundants.append(i)

  for i in range(len(abundants)):
    for j in range(len(abundants)):
      if i < j:
        sum_abundants.append(abundants[i] + abundants[j])

  numbers = [i for i in range(n + 1)]
  print sum(list(filter(lambda x: x not in sum_abundants, numbers)))

if __name__ == '__main__':
    import timeit
    ITERATIONS = 5
    MESSAGE = "Function takes {} s to complete."
    print MESSAGE.format(timeit.timeit("main()", 
                                       number=ITERATIONS, 
                                       setup="from __main__ import main") / ITERATIONS)
