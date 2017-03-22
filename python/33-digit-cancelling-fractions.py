from __future__ import division

def cancel_digits(numerator, denominator):
  n = str(numerator)
  d = str(denominator)
  union = count(n + d)
  if union != "":
    if union in d and union in n:
      if n.index(union) != d.index(union):
        n = n.replace(union, "", 1)
        d = d.replace(union, "", 1)
        if n is "" or d is "":
          return (0, 0)
        elif int(n) is 0 or int(d) is 0:
          return (0, 0)
        elif int(n) / int(d) == numerator / denominator:
          return (int(n), int(d))
        else:
          return (0, 0)
  return (0, 0)

def less_than_n (input, threshold):
  return input < threshold

def count(n):
  counter = {}
  for i in range(len(n) - 1, 0, -1):
    count = counter.get(n[i], 0)
    counter[n[i]] = count + 1
    if counter[n[i]] == 2:
      return n[i]
  return ""

n = 1
d = 1
for i in range(1, 100):
  for j in range(1, 100):
    if less_than_n(i / j, 1):
      a, b = cancel_digits(i, j)
      if a and b is not 0:
        n *= i
        d *= j
        print "Result", i, j, a, b, n, d, n / d