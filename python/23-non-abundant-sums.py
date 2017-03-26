"""
https://projecteuler.net/problem=23
"""

def is_abundant(n):
  arr = []
  for i in range(0, n):
    try:
      if n % i == 0:
        arr.append(i)
    except ZeroDivisionError:
      print "SKIP"
  return sum(arr) > n

def main():
  """
  Main
  """
  n = 28123
  sum_abundants = []
  abundants = []
  for i in range(n + 1):
    if is_abundant(i):
      print i
      abundants.append(i)

  print len(abundants)
  for i in range(len(abundants)):
    for j in range(len(abundants)):
      if i < j:
        sum_abundants.append(abundants[i] + abundants[j])

  numbers = [i for i in range(n + 1)]
  print sum(list(filter(lambda x: x not in sum_abundants, numbers)))


main()